import pymysql as ms
db= ms.connect("148.72.232.172","Test","Test#4321","Test_Antrix")
cr=db.cursor()
cr.execute("Select * from Student_Batch")
cl=cr.description
rs=cr.fetchall()
cdes=cr.description
colmn=[]
for c in cdes:
    colmn.append(c[0])
colmn
['school',
 'sex',
 'age',
 'Mjob',
 'Fjob',
 'health',
 'absences',
 'G1',
 'G2',
 'G3']
import pandas as pd
import numpy as np
df=pd.DataFrame(list(rs))
df.shape
(395, 10)
df.columns=colmn
df.head()
school	sex	age	Mjob	Fjob	health	absences	G1	G2	G3
0	GP	F	18	at_home	teacher	3	6	5	6	6
1	GP	F	17	at_home	other	3	4	5	5	6
2	GP	F	15	at_home	other	3	10	7	8	10
3	GP	F	15	health	services	5	2	15	14	15
4	GP	F	16	other	other	5	4	6	10	10
pd.pivot_table(df, index=['school'], columns=['sex'], values=['G1'],
              aggfunc=len, margins=True)
G1
sex	F	M	All
school			
GP	183	166	349
MS	25	21	46
All	208	187	395
df
school	sex	age	Mjob	Fjob	health	absences	G1	G2	G3
0	GP	F	18	at_home	teacher	3	6	5	6	6
1	GP	F	17	at_home	other	3	4	5	5	6
2	GP	F	15	at_home	other	3	10	7	8	10
3	GP	F	15	health	services	5	2	15	14	15
4	GP	F	16	other	other	5	4	6	10	10
5	GP	M	16	services	other	5	10	15	15	15
6	GP	M	16	other	other	3	0	12	12	11
7	GP	F	17	other	teacher	1	6	6	5	6
8	GP	M	15	services	other	1	0	16	18	19
9	GP	M	15	other	other	5	0	14	15	15
10	GP	F	15	teacher	health	2	0	10	8	9
11	GP	F	15	services	other	4	4	10	12	12
12	GP	M	15	health	services	5	2	14	14	14
13	GP	M	15	teacher	other	3	2	10	10	11
14	GP	M	15	other	other	3	0	14	16	16
15	GP	F	16	health	other	2	4	14	14	14
16	GP	F	16	services	services	2	6	13	14	14
17	GP	F	16	other	other	4	4	8	10	10
18	GP	M	17	services	services	5	16	6	5	5
19	GP	M	16	health	other	5	4	8	10	10
20	GP	M	15	teacher	other	1	0	13	14	15
21	GP	M	15	health	health	5	0	12	15	15
22	GP	M	16	teacher	other	5	2	15	15	16
23	GP	M	16	other	other	5	0	13	13	12
24	GP	F	15	services	health	5	2	10	9	8
25	GP	F	16	services	services	5	14	6	9	8
26	GP	M	15	other	other	5	2	12	12	11
27	GP	M	15	health	services	1	4	15	16	15
28	GP	M	16	services	other	5	4	11	11	11
29	GP	M	16	teacher	teacher	5	16	10	12	11
...	...	...	...	...	...	...	...	...	...	...
365	MS	M	18	at_home	other	3	4	10	10	10
366	MS	M	18	teacher	services	5	0	13	13	13
367	MS	F	17	other	services	1	0	7	6	0
368	MS	F	18	at_home	services	4	0	11	10	10
369	MS	F	18	other	teacher	5	10	14	12	11
370	MS	F	19	services	services	3	4	7	7	9
371	MS	M	18	at_home	services	3	3	14	12	12
372	MS	F	17	other	at_home	3	8	13	11	11
373	MS	F	17	other	other	1	14	6	5	5
374	MS	F	18	other	other	1	0	19	18	19
375	MS	F	18	other	other	4	2	8	8	10
376	MS	F	20	health	other	3	4	15	14	15
377	MS	F	18	teacher	services	2	4	8	9	10
378	MS	F	18	other	other	1	0	15	15	15
379	MS	F	17	at_home	other	1	17	10	10	10
380	MS	M	18	teacher	teacher	2	4	15	14	14
381	MS	M	18	other	other	5	5	7	6	7
382	MS	M	17	other	services	3	2	11	11	10
383	MS	M	19	other	services	5	0	6	5	0
384	MS	M	18	other	other	3	14	6	5	5
385	MS	F	18	at_home	other	4	2	10	9	10
386	MS	F	18	teacher	at_home	5	7	6	5	6
387	MS	F	19	services	other	5	0	7	5	0
388	MS	F	18	teacher	services	1	0	7	9	8
389	MS	F	18	other	other	5	0	6	5	0
390	MS	M	20	services	services	4	11	9	9	9
391	MS	M	17	services	services	2	3	14	16	16
392	MS	M	21	other	other	3	3	10	8	7
393	MS	M	18	services	other	5	0	11	12	10
394	MS	M	19	other	at_home	5	5	8	9	9
395 rows × 10 columns

df.head(1)
school	sex	age	Mjob	Fjob	health	absences	G1	G2	G3
0	GP	F	18	at_home	teacher	3	6	5	6	6
pd.pivot_table(df, index=['school'], columns=['sex'],
              values=['G1'], aggfunc=len, margins=True)
G1
sex	F	M	All
school			
GP	183	166	349
MS	25	21	46
All	208	187	395
del df['nage']
def setagecat(val):
    if val in (15,16):
        return "15-16 Years"
    elif val in (17,18):
        return "17-18 Years"
    elif val in (19,20):
        return "19-20 Years"
    elif val in (21,22):
        return "21-22 Years"
df['nage']=df['age'].map(setagecat)
df.head()
school	sex	age	Mjob	Fjob	health	absences	G1	G2	G3	n2age	nage
0	GP	F	18	at_home	teacher	3	6	5	6	6	1	17-18 Years
1	GP	F	17	at_home	other	3	4	5	5	6	1	17-18 Years
2	GP	F	15	at_home	other	3	10	7	8	10	1	15-16 Years
3	GP	F	15	health	services	5	2	15	14	15	1	15-16 Years
4	GP	F	16	other	other	5	4	6	10	10	1	15-16 Years
pd.pivot_table(df, index=['nage'],
               values=['G1'],
               aggfunc=len, margins=True)
G1
nage	
15-16 Years	186
17-18 Years	180
19-20 Years	27
21-22 Years	2
All	395
df['nage1']=df['age'].map({15:'15-16 Years',
                          16:'15-16 Years',
                          17:'17-18 Years',
                          18:'17-18 Years',
                          19:'19-20 Years',
                          20:'19-20 Years',
                          21:'21-22 Years',
                          22:'21-22 Years'
                            })
df.head()
school	sex	age	Mjob	Fjob	health	absences	G1	G2	G3	n2age	nage	nage1
0	GP	F	18	at_home	teacher	3	6	5	6	6	1	17-18 Years	17-18 Years
1	GP	F	17	at_home	other	3	4	5	5	6	1	17-18 Years	17-18 Years
2	GP	F	15	at_home	other	3	10	7	8	10	1	15-16 Years	15-16 Years
3	GP	F	15	health	services	5	2	15	14	15	1	15-16 Years	15-16 Years
4	GP	F	16	other	other	5	4	6	10	10	1	15-16 Years	15-16 Years
del df['n2age']
df.head()
school	sex	age	Mjob	Fjob	health	absences	G1	G2	G3	nage	nage1
0	GP	F	18	at_home	teacher	3	6	5	6	6	17-18 Years	17-18 Years
1	GP	F	17	at_home	other	3	4	5	5	6	17-18 Years	17-18 Years
2	GP	F	15	at_home	other	3	10	7	8	10	15-16 Years	15-16 Years
3	GP	F	15	health	services	5	2	15	14	15	15-16 Years	15-16 Years
4	GP	F	16	other	other	5	4	6	10	10	15-16 Years	15-16 Years
sr=df.groupby('nage')['nage'].count()
df1=pd.DataFrame({'Age_Category':sr.index.tolist(),
                  'Counts':sr.values.tolist()})
df1
Age_Category	Counts
0	15-16 Years	186
1	17-18 Years	180
2	19-20 Years	27
3	21-22 Years	2
df1.plot.bar(x='Age_Category',y='Counts')
<matplotlib.axes._subplots.AxesSubplot at 0x200643cd588>
