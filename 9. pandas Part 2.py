import pandas as pd
import numpy as np
ls=[[2,3,4,5],[6,7,8,9],[10,11,12,13]]
df=pd.DataFrame(ls)
df
0	1	2	3
0	2	3	4	5
1	6	7	8	9
2	10	11	12	13
df.apply(np.mean,axis=0)#column
df.apply(np.mean,axis=1)#row
0     3.5
1     7.5
2    11.5
dtype: float64
def getadd(val):
    print(type(val))
    return val+10
def getadd1(val):
    if val%2==0:
        return val*20
    else:
        return val
#df.applymap(getadd1)
df
0	1	2	3
0	2	3	4	5
1	6	7	8	9
2	10	11	12	13
def getmax(val):
    return np.max(val)
#df.apply(lambda x:np.max(x),1)
#df.apply(getmax)
df.apply(lambda x:np.max(x)-np.min(x),1) #1-Row , 0 - Column
0    3
1    3
2    3
dtype: int64
df.pipe(lambda x:x.sum()) #column wise sum
0    18
1    21
2    24
3    27
dtype: int64
df.applymap(lambda x:x+20)
0	1	2	3
0	22	23	24	25
1	26	27	28	29
2	30	31	32	33
print(df)
df[0].apply(getadd,0)
    0   1   2   3
0   2   3   4   5
1   6   7   8   9
2  10  11  12  13
<class 'int'>
<class 'int'>
<class 'int'>
0    12
1    16
2    20
Name: 0, dtype: object
df
0	1	2	3
0	2	3	4	5
1	6	7	8	9
2	10	11	12	13
df.sum(1)
0    14
1    30
2    46
dtype: int64
df['Name'] =['A','A','C']
print(df)
#df.describe()
print("---------")
print(df.describe())
print("---------")
print(df.describe(include='object'))
print("---------")
print(df.describe(include='all'))
    0   1   2   3 Name
0   2   3   4   5    A
1   6   7   8   9    A
2  10  11  12  13    C
---------
          0     1     2     3
count   3.0   3.0   3.0   3.0
mean    6.0   7.0   8.0   9.0
std     4.0   4.0   4.0   4.0
min     2.0   3.0   4.0   5.0
25%     4.0   5.0   6.0   7.0
50%     6.0   7.0   8.0   9.0
75%     8.0   9.0  10.0  11.0
max    10.0  11.0  12.0  13.0
---------
       Name
count     3
unique    2
top       A
freq      2
---------
           0     1     2     3 Name
count    3.0   3.0   3.0   3.0    3
unique   NaN   NaN   NaN   NaN    2
top      NaN   NaN   NaN   NaN    A
freq     NaN   NaN   NaN   NaN    2
mean     6.0   7.0   8.0   9.0  NaN
std      4.0   4.0   4.0   4.0  NaN
min      2.0   3.0   4.0   5.0  NaN
25%      4.0   5.0   6.0   7.0  NaN
50%      6.0   7.0   8.0   9.0  NaN
75%      8.0   9.0  10.0  11.0  NaN
max     10.0  11.0  12.0  13.0  NaN
dfa=pd.DataFrame({'Name':['A','B','C','D'],'Age':[20,30,40,60]})
dfa
Age	Name
0	20	A
1	30	B
2	40	C
3	60	D
dfb=pd.DataFrame({'Name':['X','Y','Z'],'Age':[20,30,40],'Sub':['Python','SAS','Python']})
dfb
Age	Name	Sub
0	20	X	Python
1	30	Y	SAS
2	40	Z	Python
d={'A':dfa, 'B':dfb}
d
{'A':    Age Name
 0   20    A
 1   30    B
 2   40    C
 3   60    D, 'B':    Age Name     Sub
 0   20    X  Python
 1   30    Y     SAS
 2   40    Z  Python}
pn=pd.Panel(d)
pn
<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 4 (major_axis) x 3 (minor_axis)
Items axis: A to B
Major_axis axis: 0 to 3
Minor_axis axis: Age to Sub
pn['A']
Age	Name	Sub
0	20	A	NaN
1	30	B	NaN
2	40	C	NaN
3	60	D	NaN
pn['B']
Age	Name	Sub
0	20	X	Python
1	30	Y	SAS
2	40	Z	Python
3	NaN	NaN	NaN
pn.major_xs(2)
A	B
Age	40	40
Name	C	Z
Sub	NaN	Python
pn.minor_xs('Age')
A	B
0	20	20
1	30	30
2	40	40
3	60	NaN
ls=[1,2,3,4,5]
sr=pd.Series(ls, dtype=float)
sr
0    1.0
1    2.0
2    3.0
3    4.0
4    5.0
dtype: float64
sr.ndim #dimension
sr.size #no of elements
sr.itemsize #memory size of individual element
sr.shape #shape of collection
sr.values #values of series
sr.index.tolist() #index of series
sr.head(1)
sr.tail(1)
sr.dtype #to view the datatype of series
dtype('float64')
df.T #transpose of data
df.shape
(3, 5)
df
0	1	2	3	Name
0	2	3	4	5	A
1	6	7	8	9	A
2	10	11	12	13	C
df['CS']=df[0].cumsum()
df
0	1	2	3	Name	CS
0	2	3	4	5	A	2
1	6	7	8	9	A	8
2	10	11	12	13	C	18
del df['Name']
df
0	1	2	3	CS
0	2	3	4	5	2
1	6	7	8	9	8
2	10	11	12	13	18
df.apply(np.max,1)
0     5
1     9
2    18
dtype: int64
df.apply(np.min,1)
0     2
1     6
2    10
dtype: int64
def getrange(val):
    return np.max(val)-np.min(val)
df.apply(getrange)
0      8
1      8
2      8
3      8
CS    16
dtype: int64
df.apply(lambda x:np.max(x)-np.min(x))
0      8
1      8
2      8
3      8
CS    16
dtype: int64
df.apply(lambda x:x.max()-x.min())
0      8
1      8
2      8
3      8
CS    16
dtype: int64
df
0	1	2	3	CS
0	2	3	4	5	2
1	6	7	8	9	8
2	10	11	12	13	18
df.applymap(lambda x:x+10)
0	1	2	3	CS
0	12	13	14	15	12
1	16	17	18	19	18
2	20	21	22	23	28
df.pipe(lambda x:x+10)
0	1	2	3	CS
0	12	13	14	15	12
1	16	17	18	19	18
2	20	21	22	23	28
def getmsg(val):
    print(type(val))
df.pipe(getmsg)
<class 'pandas.core.frame.DataFrame'>
df.apply(getmsg,1)
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
0    None
1    None
2    None
dtype: object
df.applymap(getmsg)
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
0	1	2	3	CS
0	None	None	None	None	None
1	None	None	None	None	None
2	None	None	None	None	None
df
0	1	2	3	CS
0	2	3	4	5	2
1	6	7	8	9	8
2	10	11	12	13	18
df.iloc[[0,1],[0,1,2]]
0	1	2
0	2	3	4
1	6	7	8
df.reindex(index=[0,1], columns=[0,1,2])
0	1	2
0	2	3	4
1	6	7	8
df.rename(columns={0:'C1'}, index={0:'R1'})
C1	1	2	3	CS
R1	2	3	4	5	2
1	6	7	8	9	8
2	10	11	12	13	18
for d in df:
    print(d)
0
1
2
3
CS
for d in df:
    print(df[d])
0     2
1     6
2    10
Name: 0, dtype: int64
0     3
1     7
2    11
Name: 1, dtype: int64
0     4
1     8
2    12
Name: 2, dtype: int64
0     5
1     9
2    13
Name: 3, dtype: int64
0     2
1     8
2    18
Name: CS, dtype: int64
for d in df.iteritems(): #column wise data 
    #print(d)
    print("Column Index", d[0])
    print(d[1])
    print("-----------")
Column Index 0
0     2
1     6
2    10
Name: 0, dtype: int64
-----------
Column Index 1
0     3
1     7
2    11
Name: 1, dtype: int64
-----------
Column Index 2
0     4
1     8
2    12
Name: 2, dtype: int64
-----------
Column Index 3
0     5
1     9
2    13
Name: 3, dtype: int64
-----------
Column Index CS
0     2
1     8
2    18
Name: CS, dtype: int64
-----------
for d in df.iterrows(): #column wise data 
    #print(d)
    print("Rows Index", d[0])
    print(d[1])
    print("-----------")
Rows Index 0
0     2
1     3
2     4
3     5
CS    2
Name: 0, dtype: int64
-----------
Rows Index 1
0     6
1     7
2     8
3     9
CS    8
Name: 1, dtype: int64
-----------
Rows Index 2
0     10
1     11
2     12
3     13
CS    18
Name: 2, dtype: int64
-----------
for d in df.itertuples():
    print(d)
Pandas(Index=0, _1=2, _2=3, _3=4, _4=5, CS=2)
Pandas(Index=1, _1=6, _2=7, _3=8, _4=9, CS=8)
Pandas(Index=2, _1=10, _2=11, _3=12, _4=13, CS=18)
ls=['rajeev','Rajeev','raj@gmail.com', ' Raj']
sr=pd.Series(ls)
sr
0           rajeev
1           Rajeev
2    raj@gmail.com
3              Raj
dtype: object
sr1="rajeev"
sr1[0].upper()+sr1[1:]
'Rajeev'
sr.str.upper()
sr.str.lower()
sr.str.len()
0     6
1     6
2    13
3     4
dtype: int64
def getUpdatedName(val):
    st1=val
    return st1[0].upper()+st1[1:]    
df1[0].map(getUpdatedName)
0           Rajeev
1           Rajeev
2    Raj@gmail.com
3              Raj
Name: 0, dtype: object
df1=pd.DataFrame(sr)
df1[0].map(lambda x:x[0].upper()+x[1:])
0           Rajeev
1           Rajeev
2    Raj@gmail.com
3              Raj
Name: 0, dtype: object
ls=['rajeev','rajeev','raj@gmail.com', ' Raj']
sr=pd.Series(ls)
sr
sr.str.upper()
sr.str.lower()
sr.str.len()
sr1=sr.str.strip()
sr.str.split('@')
sr.str.cat(sep='--') 
sr.str.get_dummies()
sr.str.contains('@')
sr.str.replace('@','#')
sr.str.repeat(2)
sr.str.startswith('r')
sr.str.endswith('r')
0    False
1    False
2    False
3    False
dtype: bool
sr2='Satish Kumar'
sr2+ " Hello "
#sr.replace('S','Z')
#sr.split(' ')
'Satish Kumar Hello '
sr1.str.len()
0     6
1     6
2    13
3     3
dtype: int64