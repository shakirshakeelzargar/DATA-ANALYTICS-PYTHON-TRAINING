import csv
import datetime
import requests
import sys
import wget
from azure.storage.blob import BlockBlobService
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.documents as documents
import json
import azure.functions as func
import logging
import uuid

def main(msg: func.QueueMessage,  context: func.Context) -> None:
	logging.info('Python queue trigger function processed a queue item: %s',
                 msg.get_body().decode('utf-8'))
	queuemg=msg.get_json()
	client=""
	actionType=""
	if 'Client' in queuemg:
		client=queuemg['Client']
	if 'actionType' in queuemg:
		actionType=queuemg['actionType']
	if client == '' or actionType=='':
		print('ActionType, Client and ReportType are required parameters....')
		return
	currDir=context.function_directory
	invocationId=context.invocation_id
    #guid=str(uuid.uuid4())  

	inputDate = datetime.datetime.now() 
	with open(currDir + '/configSettingsDEV.json') as config_file:
		configSettings=json.load(config_file)
    
	db_lnk= 'dbs/' + configSettings['cosmosDB']['databaseName']  
	dbclient = cosmos_client.CosmosClient(url_connection=configSettings['cosmosDB']['documentDBUri'], auth={'masterKey': configSettings['cosmosDB']['documentDBSecretKey']})

	query = {
        "query": "SELECT * FROM r WHERE r.client=@client",
        "parameters": [ { "name":"@client", "value": client } ]
    }
    #options = {'maxItemCount': 1000, 'continuation': True}
	innovidcoll_link=db_lnk + '/colls/InnovidConfigNew'
	docs = list(dbclient.QueryItems(innovidcoll_link, query))

	for item in iter(docs):
		innovid_config=item 

	storagecoll_link=db_lnk + '/colls/Storage'
	docs = list(dbclient.QueryItems(storagecoll_link, query))

	for item in iter(docs):
	   storage_config=item
	   
	if (innovid_config is None or storage_config is None) :
		print('Innovid/Storage configuration missing for client ' + client)
		return 
	log={}
	log["client"] =client
	log["cloudLocation"] =json.dumps(innovid_config["storage"])
	log["dataSource"] = "Innovid"
	log["docTitle"] =innovid_config["title"]
   
	log["ConnectionType"] ="API"
	log["lastRun"] =datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
	log["queueMessage"] =json.dumps(queuemg)

	blob_service = BlockBlobService(account_name=storage_config['blobStorage']['accountName'], account_key=storage_config['blobStorage']['accountKey'])    
	container_name=storage_config['blobStorage']['containerName']    
	requestlogPath=innovid_config['requestlog'].replace('#yyyy#',inputDate.strftime("%Y")).replace('#MM#',inputDate.strftime("%m")).replace('#dd#',inputDate.strftime("%d"))
	retrieverlogPath=innovid_config['retrieverlog'].replace('#yyyy#',inputDate.strftime("%Y")).replace('#MM#',inputDate.strftime("%m")).replace('#dd#',inputDate.strftime("%d"))    
	request_filename='innovidRequest_' + inputDate.strftime('%Y-%m-%d') + '_Run.csv'
	retrieverLogFileName ='innovid_' + client + inputDate.strftime('%Y-%m-%d') + '_' + actionType + '.log'
	request_blob_path=requestlogPath + request_filename
	log["retriverLogFullPath"] = retrieverlogPath
	log["retriverLogFileName"] = retrieverLogFileName
	log["requestLogFullPath"] =requestlogPath
	log["requestLogFileName"] =request_filename
	log["actionType"] = actionType

	print(request_blob_path)
	if(actionType=="Run"):
		RunReport(client,actionType,inputDate,container_name,request_blob_path,innovid_config,blob_service,log)           

	if(actionType=="Download"):        
		DownloadReport(client,actionType,inputDate,container_name,request_blob_path,currDir,request_filename,blob_service,innovid_config,log)
        #upload log to retriever log path
	blob_service.create_blob_from_text(container_name, retrieverlogPath+retrieverLogFileName, json.dumps(log))

	retrieverlogcolllnk=db_lnk + '/colls/RetrieverLogs'
	dbclient.CreateItem(retrieverlogcolllnk, log)

def RunReport(client,actionType,inputDate,container_name,request_blob_path,innovid_config,blob_service,log):
	try:
		filecontent="Request_URL,Report_Code,Report_Blob_path\n"
		URL = 'https://papi.innovid.com/v2/advertisers'            
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		r = requests.get(URL, headers=headers, auth=(innovid_config['authentication']['username'],innovid_config['authentication']['password']))             
		respData = r.json()
		start_date = inputDate
		print(start_date)            

		for cli in respData['data']['clients'] :
			clientId=str(cli["id"])
			for ad in cli["advertisers"]:
				for report in innovid_config['reports']:
					log["ReportType"] =report['reportType']
					log["lookBackWindow"] =report['lookBackWindow']                        
					advertiserId=str(ad["id"])
					end_date = start_date + datetime.timedelta(days=int(report['lookBackWindow'])*-1)
					print('start amd emd dates')
					print(start_date.date())
					print(end_date.date())

					URL=''
					if report['reportType']=='deliveryreports':                        
						URL = 'https://papi.innovid.com/v2/clients/' + clientId + '/advertisers/' + advertiserId + '/reports/delivery/dateFrom/' + end_date.strftime('%Y-%m-%d') + '/dateTo/' + start_date.strftime('%Y-%m-%d')
					if report['reportType'] == 'viewabilityreports':
						URL = 'https://papi.innovid.com/v2/clients/' + clientId + '/advertisers/' + advertiserId + '/reports/viewability/dateFrom/' + end_date.strftime('%Y-%m-%d') + '/dateTo/' + start_date.strftime('%Y-%m-%d')

					headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
					r = requests.get(URL, headers=headers, auth=(innovid_config['authentication']['username'],innovid_config['authentication']['password'])) 

					respData = r.json()
					print(respData)
					filecontent =filecontent + URL + "," + respData['data']['reportStatusToken'] + "," + report["fileFolder"] + "\n"


		print('Completed Processing all File for Given Date.')
		blob_service.create_blob_from_text(container_name, request_blob_path, filecontent)            
		log["status"] ="Success"
	except Exception as ex:
		log["status"] ="Failed"

def DownloadReport(client,actionType,inputDate,container_name,request_blob_path,currDir,request_filename,blob_service,innovid_config,log):
	try:
		start_date = inputDate        
		blob_service.get_blob_to_path(container_name,request_blob_path,currDir + '/request/' +request_filename)
		with open(currDir + '/request/' + request_filename) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0            
			filecontent="Request_URL,Status_URL,Report_URL\n"
			for row in csv_reader:
				if line_count == 0:
					print('Column names are {", ".join(row)}')
					line_count += 1
				else:
					print('\t https://papi.innovid.com/v2/reports/{row[1]}/status')
					URL = 'https://papi.innovid.com/v2/reports/' + row[1] + '/status'                
					line_count += 1
					headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
					r = requests.get(URL, headers=headers, auth=(innovid_config['authentication']['username'],innovid_config['authentication']['password'])) 
					
					respData = r.json()                   

					if(respData['data']['reportStatus']=="READY"):
						reportURL=respData['data']['reportUrl']
						urlData = row[0].split('/')
						print(reportURL)
						filename = urlData[5] + "_" + urlData[7] + "_" + urlData[9] + "_" + urlData[11] + "_" + urlData[13] + ".zip" 
						
						wget.download(reportURL,currDir +"/downloads/" + filename)

						 # Upload file to blob                        
						local_file_full_path=currDir + "/downloads/" + filename                        
						blob_file_path=row[2].replace('#yyyy#',inputDate.strftime("%Y")).replace('#MM#',inputDate.strftime("%m")).replace('#dd#',inputDate.strftime("%d"))
						blob_full_path = blob_file_path + filename                      
						blob_service.create_blob_from_path(container_name,blob_full_path,local_file_full_path)
						
						print(filename + ' uploaded to blob')

						filecontent= filecontent+  row[0] + "," + URL + "," + respData['data']['reportUrl'] + "\n"                    

			print('Completed Processing all File for Given Date.')
			log["status"] ="Success"
	except Exception as ex:
		log["status"]="Failed"
		log["errorMessge"] =ex