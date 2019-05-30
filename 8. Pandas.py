import pandas as pd
ls=[14,15,16,17]
sr=pd.Series(ls)
print(ls)
print("--------")
print(sr)
print("--------")
print("Index ", sr.index.tolist())
print("--------")
sr[0]=44
print("Values ", sr.values.tolist())
[14, 15, 16, 17]
--------
0    14
1    15
2    16
3    17
dtype: int64
--------
Index  [0, 1, 2, 3]
--------
Values  [44, 15, 16, 17]
ls=[14,15,16,17]
sr=pd.Series(ls,index=['A','B','C','D'])
print(sr)
print("-------")
print(sr[0])
print(sr['A'])
A    14
B    15
C    16
D    17
dtype: int64
-------
14
14
ls=[14,15,16,17]
sr=pd.Series(ls,index=[21,22,23,24])
print(sr)
print("-------")
print(sr[21])
21    14
22    15
23    16
24    17
dtype: int64
-------
14
sr=pd.Series([14,15,16,17],
             index=[21,22,23,24], 
             dtype=float)
print(sr)
print("-------")
print(sr.dtype)
21    14.0
22    15.0
23    16.0
24    17.0
dtype: float64
-------
float64
ls=[['Rajeev',40,89],['Manish',30,98]]
df=pd.DataFrame(ls, columns=['Name','Age','Marks'],
               index=['R1','R2'])
df
Name	Age	Marks
R1	Rajeev	40	89
R2	Manish	30	98
d={'Name':['Rajeev','Manish'], 'Age':[40,30],'Marks':[89,98]}
df=pd.DataFrame(d)
df
Age	Marks	Name
0	40	89	Rajeev
1	30	98	Manish
df['Final_Marks']=df['Marks']*.40
df
Name	Age	Marks	Final_Marks
R1	Rajeev	40	89	35.6
R2	Manish	30	98	39.2
#column filter
#df.Name
df['Name']
df[['Name','Final_Marks']]
Name	Final_Marks
0	Rajeev	35.6
1	Manish	39.2
#df.info() #structure
#df.dtypes #datatype of columns
#df.columns #column names
#df.values.tolist()
#df.index.tolist()
['R1', 'R2']
#Rows filter
#index wise 
#df.loc['R1']
#df.loc[['R1','R2']]
#df.iloc[0]
#df.iloc[[0,1]]
#df.iloc[0:2,0:4]
df.iloc[0:2:1,0:4:2]

#date wise
#df1=df.query('Marks>90 or Age>35')
#df[[False,True]]
#df[df['Marks']>90]
Name	Marks
R1	Rajeev	89
R2	Manish	98
df=pd.read_csv("d:/d/testsalesretail.csv")
#df.head(1)
df.tail()
Account	Name	Rep	Manager	Product	Quantity	Price	Status
12	239344	Stokes LLC	Cedric Moss	Fred Anderson	Software	1	10000	presented
13	307599	Kassulke, Ondricka and Metz	Wendy Yule	Fred Anderson	Maintenance	3	7000	won
14	688981	Keeling LLC	Wendy Yule	Fred Anderson	CPU	5	100000	won
15	729833	Koepp Ltd	Wendy Yule	Fred Anderson	CPU	2	65000	declined
16	729833	Koepp Ltd	Wendy Yule	Fred Anderson	Monitor	2	5000	presented
#df.groupby('Manager')['Price'].sum()
df.groupby(['Manager','Product'])['Price','Quantity'].sum()
Price	Quantity
Manager	Product		
Debra Henley	CPU	205000	7
Maintenance	10000	4
Software	20000	2
Fred Anderson	CPU	260000	10
Maintenance	12000	4
Monitor	5000	2
Software	10000	1
df1=df[['Manager','Product','Price']]
df1.head(1)
Manager	Product	Price
0	Debra Henley	CPU	30000
ls=[['Rajeev',60,89],['Aman',70,19],['Satish',80,69]]
ls
[['Rajeev', 60, 89], ['Aman', 70, 19], ['Satish', 80, 69]]
df3=pd.DataFrame(ls, columns=['C','A','B'],
                index=[3,1,2])
df3
C	A	B
3	Rajeev	60	89
1	Aman	70	19
2	Satish	80	69
#df3.sort_index() #row index wise sorting
#df3.sort_index(1) #columns index wise sorting
#df3.sort_index(1, ascending=False) #columns index wise sorting
df3.sort_values(by='A',ascending=False)
C	A	B
2	Satish	80	69
1	Aman	70	19
3	Rajeev	60	89
df4=df1[['Product', 'Manager','Price']].sort_values(by=['Product','Manager','Price'])
df4.head(1)
Product	Manager	Price
0	CPU	Debra Henley	30000
del df4['Manager'] #deleting columns
df4.head()
Product	Price
0	CPU	30000
3	CPU	35000
8	CPU	35000
5	CPU	40000
4	CPU	65000
rs=df4.pop('Product')
rs
0             CPU
3             CPU
8             CPU
5             CPU
4             CPU
10            CPU
9             CPU
15            CPU
14            CPU
2     Maintenance
7     Maintenance
11    Maintenance
13    Maintenance
16        Monitor
1        Software
6        Software
12       Software
Name: Product, dtype: object
df4['Product']=rs
df4
Price	Product
0	30000	CPU
3	35000	CPU
8	35000	CPU
5	40000	CPU
4	65000	CPU
10	30000	CPU
9	65000	CPU
15	65000	CPU
14	100000	CPU
2	5000	Maintenance
7	5000	Maintenance
11	5000	Maintenance
13	7000	Maintenance
16	5000	Monitor
1	10000	Software
6	10000	Software
12	10000	Software
df4.dtypes
Price       int64
Product    object
dtype: object
print(df4.head())
df4=df4.drop(3)
print(df4.head())
   Price Product
0  30000     CPU
3  35000     CPU
8  35000     CPU
5  40000     CPU
4  65000     CPU
    Price Product
0   30000     CPU
8   35000     CPU
5   40000     CPU
4   65000     CPU
10  30000     CPU
df4.shape
(16, 2)
df4=df4.query('Price<30000')
df4.shape
(8, 2)
df5=df4.query('Price<10000')
ls2=df5.index.tolist()
df4=df4.drop(ls2)
df4.shape
(3, 2)
df4
Price	Product
1	10000	Software
6	10000	Software
12	10000	Software
df=pd.read_csv("d:/d/testsalesretail.csv")
df.shape
(17, 8)
df.head(1)
Account	Name	Rep	Manager	Product	Quantity	Price	Status
0	714466	Trantow-Barrows	Craig Booker	Debra Henley	CPU	1	30000	presented
#1- Manager wise Total Sales [Price *Quantity]
#2- Product wise Total Sales
#3 - Manager, Product wise Total Sales
#4 - Plot above values - 1-> Pie, -2 Line , -3 Bar
df['Sales'] =df['Price']*df['Quantity']
df.dtypes
Account      int64
Name        object
Rep         object
Manager     object
Product     object
Quantity     int64
Price        int64
Status      object
Sales        int64
dtype: object
df.head(1)
Account	Name	Rep	Manager	Product	Quantity	Price	Status	Sales
0	714466	Trantow-Barrows	Craig Booker	Debra Henley	CPU	1	30000	presented	30000
#1- Manager wise Total Sales [Price *Quantity]
sr_mgr=df.groupby('Manager')['Sales'].sum()
sr_mgr
Manager
Debra Henley     350000
Fred Anderson    836000
Name: Sales, dtype: int64
#2- Product wise Total Sales
sr_prd=df.groupby('Product')['Sales'].sum()
sr_prd
Product
CPU            1100000
Maintenance      46000
Monitor          10000
Software         30000
Name: Sales, dtype: int64
#3 - Manager, Product wise Total Sales
sr_mgrprd=df.groupby(['Manager','Product'])['Sales'].sum()
sr_mgrprd
Manager        Product    
Debra Henley   CPU            310000
               Maintenance     20000
               Software        20000
Fred Anderson  CPU            790000
               Maintenance     26000
               Monitor         10000
               Software        10000
Name: Sales, dtype: int64
#4 - Plot above values - 1-> Pie, -2 Line , -3 Bar
import matplotlib.pyplot as plt
lx_index=sr_mgr.index.tolist()
ly_values=sr_mgr.values.tolist()
print(lx_index)
print(ly_values)
['Debra Henley', 'Fred Anderson']
[350000, 836000]
plt.pie(ly_values, labels=lx_index)
plt.show()

lx_index=sr_prd.index.tolist()
ly_values=sr_prd.values.tolist()
print(lx_index)
print(ly_values)
['CPU', 'Maintenance', 'Monitor', 'Software']
[1100000, 46000, 10000, 30000]
plt.plot(lx_index,ly_values)
plt.show()

lx_label= sr_mgrprd.index.tolist()
lx_label
lx1=[]
for l in lx_label:
    lx1.append(l[0]+"-"+l[1])
print(lx1)
['Debra Henley-CPU', 'Debra Henley-Maintenance', 'Debra Henley-Software', 'Fred Anderson-CPU', 'Fred Anderson-Maintenance', 'Fred Anderson-Monitor', 'Fred Anderson-Software']
lx_label[0][0]
('Debra Henley', 'CPU')
for a in range(len(lx_label)):
    #print(lx_label[a][0])
    if lx_label[a][0]=="Debra Henley":
        plt.bar(lx1[a], ly_label[a], color='blue')
    else:
        plt.bar(lx1[a], ly_label[a], color='red')
    plt.annotate(xy=[lx1[a], ly_label[a]+10000], s=ly_label[a])
plt.xticks(lx1, lx1,rotation='vertical') 
plt.ylim(0,1000000)
plt.show()

plt.bar(lx1, ly_label)
plt.xticks(lx1, lx1,rotation='vertical') 
plt.show()

df3=pd.DataFrame(ls, columns=['C','A','B'],
                index=[3,1,2])
df3
C	A	B
3	Rajeev	60	89
1	Aman	70	19
2	Satish	80	69
df4=pd.DataFrame(ls, columns=['C','D','B'],
                index=[3,6,2])
df4
C	D	B
3	Rajeev	60	89
6	Aman	70	19
2	Satish	80	69
df3=df3.append(df4)
df3['E']=df3['B']+df3['D']
df3
A	B	C	D	E
3	60.0	89	Rajeev	NaN	NaN
1	70.0	19	Aman	NaN	NaN
2	80.0	69	Satish	NaN	NaN
3	NaN	89	Rajeev	60.0	149.0
6	NaN	19	Aman	70.0	89.0
2	NaN	69	Satish	80.0	149.0
df3['E'].isnull()
3     True
1     True
2     True
3    False
6    False
2    False
Name: E, dtype: bool