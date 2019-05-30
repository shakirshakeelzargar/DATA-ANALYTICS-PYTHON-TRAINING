f=open("d:/d/Test3.txt","rb")
#f.read()
print(f.read(5))
print("Current Cursor Position ", f.tell())
#f.seek(0,0) #reading after setting cursor at starting of the file and 0 movement
#f.seek(3,0) #reading after settingcursor at starting of the file and 2 movement
#f.seek(2,1) #reading after setting cursor at current of the file and 2 movement
f.seek(-5,2) #reading after setting cursor at end of the file and -5 movement
print("Changed Cursor Position ", f.tell())
print(f.read(5))
print("Current Cursor Position ", f.tell())
b'INDIA'
Current Cursor Position  5
Changed Cursor Position  22
b'mming'
Current Cursor Position  27
f=open('d:/d/test4.txt')
sr=f.readlines()
print(type(sr))
print(sr)
for l in sr:
    print(l)
<class 'list'>
['Indian\n', 'UK\n', 'Pakistan\n', 'USA']
Indian

UK

Pakistan

USA
#TestSalesRetail2
#Account,Name,Rep,Manager,Product,Quantity,Price,Status
f=open("d:/d/TestSalesRetail2.csv")
ls=f.readlines()
lproduct=[]
ltotal=[]
lmgr=[]
lstatus=[]
for l in ls[1:]:
    rw=l.split(",")
    lproduct.append(rw[4])
    lmgr.append(rw[3])
    lstatus.append(rw[7])
    ltotal.append(int(rw[5])*int(rw[6]))
#print(lproduct)
#print(ltotal)
#print(lmgr)
d={}
for a in range(len(lproduct)):   
    #print()
    if lproduct[a]+":"+lstatus[a] not in d.keys():
        d[lproduct[a]+":"+lstatus[a]]=ltotal[a]
    else:   
        d[lproduct[a]+":"+lstatus[a]] =d[lproduct[a]+":"+lstatus[a]]+ltotal[a]

print(d)  
{'CPU:presented\n': 60000, 'Software:presented\n': 30000, 'Maintenance:pending\n': 25000, 'CPU:declined\n': 200000, 'CPU:won\n': 760000, 'CPU:pending\n': 80000, 'Maintenance:won\n': 21000, 'Monitor:presented\n': 10000}
st="abc\n"
print(st)
st=st.replace('\n','')
print(st)
abc

abc
d={}
for a in range(len(lproduct)):   
    #print()
    if lmgr[a]+":"+lproduct[a] not in d.keys():
        d[lmgr[a]+":"+lproduct[a]]=ltotal[a]
    else:   
        d[lmgr[a]+":"+lproduct[a]] =d[lmgr[a]+":"+lproduct[a]]+ltotal[a]
d={}
for a in range(len(lproduct)):
    #print("Position ", a)
    #print("Product  :", lproduct[a])
    #print("Total  :", ltotal[a])
    if lproduct[a] not in d.keys():
        #print("Add New Key in Dict ", lproduct[a], " Value ", ltotal[a])
        
        d[lproduct[a]]=ltotal[a]
        #print(d)
    else:
        #print("Updating Key in Dict ", lproduct[a], " adding Value ", ltotal[a])
        d[lproduct[a]] =d[lproduct[a]]+ltotal[a]
        #print(d)
    #print("----------")
print(d)
{'CPU': 1100000, 'Software': 30000, 'Maintenance': 46000, 'Monitor': 10000}
d={}
for a in range(len(lproduct)):   
    #print()
    if lmgr[a]+":"+lproduct[a] not in d.keys():
        d[lmgr[a]+":"+lproduct[a]]=ltotal[a]
    else:   
        d[lmgr[a]+":"+lproduct[a]] =d[lmgr[a]+":"+lproduct[a]]+ltotal[a]
 
       
for a in d.keys():
    print(a, d[a])
Debra Henley:CPU 310000
Debra Henley:Software 20000
Debra Henley:Maintenance 20000
Fred Anderson:CPU 790000
Fred Anderson:Maintenance 26000
Fred Anderson:Software 10000
Fred Anderson:Monitor 10000