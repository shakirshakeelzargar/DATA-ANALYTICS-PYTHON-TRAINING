import pandas as pd
df=pd.read_excel("d:/d/regressionbook1.xlsx")
df
Sales	Mark_Exp	Hr_Cost
0	100	10	20
1	110	11	22
2	120	15	21
3	130	14	22
4	140	17	23
5	150	18	24
6	160	19	20
7	170	19	23
from sklearn import linear_model
reg=linear_model.LinearRegression()
reg.fit(df[['Mark_Exp']],df['Sales']) #input, output
reg.score(df[['Mark_Exp']],df['Sales'])
0.9166839952866153
print(df['Mark_Exp'].ndim)
print("------")
print(df[['Mark_Exp']].ndim)
1
------
2
df['Pre_Sales']=reg.predict(df[['Mark_Exp']])
df['Var']=df['Sales']-df['Pre_Sales']
df
Sales	Mark_Exp	Hr_Cost	Pre_Sales	Var
0	100	10	20	99.010189	0.989811
1	110	11	22	105.705968	4.294032
2	120	15	21	132.489083	-12.489083
3	130	14	22	125.793304	4.206696
4	140	17	23	145.880640	-5.880640
5	150	18	24	152.576419	-2.576419
6	160	19	20	159.272198	0.727802
7	170	19	23	159.272198	10.727802
lsexp=[20,20.5,21]
df1=pd.DataFrame({'Expense':lsexp})
df1['Sales']=reg.predict(df1[['Expense']])
df1
Expense	Sales
0	20.0	165.967977
1	20.5	169.315866
2	21.0	172.663755
from sklearn import linear_model
reg=linear_model.LinearRegression()
reg.fit(df[['Mark_Exp']+['Hr_Cost']],df['Sales']) #input, output
reg.score(df[['Mark_Exp']+['Hr_Cost']],df['Sales'])
0.9181453809634992
df['Pre_Sales1']=reg.predict(df[['Mark_Exp']+['Hr_Cost']])
df
Sales	Mark_Exp	Hr_Cost	Pre_Sales	Var	Pre_Sales1
0	100	10	20	99.010189	0.989811	98.325940
1	110	11	22	105.705968	4.294032	106.307495
2	120	15	21	132.489083	-12.489083	131.919216
3	130	14	22	125.793304	4.206696	126.042494
4	140	17	23	145.880640	-5.880640	146.479103
5	150	18	24	152.576419	-2.576419	153.759047
6	160	19	20	159.272198	0.727802	157.530936
7	170	19	23	159.272198	10.727802	159.635769
lsexp=[20,20.5,21]
lshrcost=[21,22,23]
df1=pd.DataFrame({'Expense':lsexp,'HrCost':lshrcost})
df1['Sales']=reg.predict(df1[['Expense']+['HrCost']])
df1
Expense	HrCost	Sales
0	20.0	21	164.810880
1	20.5	22	168.801658
2	21.0	23	172.792435