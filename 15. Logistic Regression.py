import pandas as pd
df=pd.read_csv("creditcard.csv")
df.head(1)
Time	V1	V2	V3	V4	V5	V6	V7	V8	V9	...	V21	V22	V23	V24	V25	V26	V27	V28	Amount	Class
0	0.0	-1.359807	-0.072781	2.536347	1.378155	-0.338321	0.462388	0.239599	0.098698	0.363787	...	-0.018307	0.277838	-0.110474	0.066928	0.128539	-0.189115	0.133558	-0.021053	149.62	0
1 rows × 31 columns

df.shape
(284807, 31)
df.columns
Index(['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
       'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
       'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount',
       'Class'],
      dtype='object')
df.groupby('Class')['Class'].count()
Class
0    284315
1       492
Name: Class, dtype: int64
dfinput=df.iloc[:,:-1]
dfinput.shape
dfinput.columns
Index(['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
       'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
       'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount'],
      dtype='object')
dfoutput=df.iloc[:,-1]
dfoutput.shape
dfoutput.head(5)
0    0
1    0
2    0
3    0
4    0
Name: Class, dtype: int64
df.shape
(284807, 31)
from sklearn import linear_model
reg=linear_model.LogisticRegression()
reg.fit(dfinput, dfoutput)
reg.score(dfinput, dfoutput)
0.9990239003957065
df['pre_class']=reg.predict(dfinput)
df.head(2)
Time	V1	V2	V3	V4	V5	V6	V7	V8	V9	...	V22	V23	V24	V25	V26	V27	V28	Amount	Class	pre_class
0	0.0	-1.359807	-0.072781	2.536347	1.378155	-0.338321	0.462388	0.239599	0.098698	0.363787	...	0.277838	-0.110474	0.066928	0.128539	-0.189115	0.133558	-0.021053	149.62	0	0
1	0.0	1.191857	0.266151	0.166480	0.448154	0.060018	-0.082361	-0.078803	0.085102	-0.255425	...	-0.638672	0.101288	-0.339846	0.167170	0.125895	-0.008983	0.014724	2.69	0	0
2 rows × 32 columns

df.groupby(['Class','pre_class'])['Class'].count()
Class  pre_class
0      0            284240
       1                75
1      0               203
       1               289
Name: Class, dtype: int64
df0=df.query("Class==0")
df0.shape
(284315, 32)
df1=df.query("Class==1")
df1.shape
(492, 32)
dftest0=df0.iloc[0:100]
dftest0.shape
(100, 32)
dftest1=df1.iloc[0:100]
dftest1.shape
(100, 32)
dftest0=dftest0.append(dftest1)
dftest0.shape
(200, 32)
df.head(1)
Time	V1	V2	V3	V4	V5	V6	V7	V8	V9	...	V22	V23	V24	V25	V26	V27	V28	Amount	Class	pre_class
0	0.0	-1.359807	-0.072781	2.536347	1.378155	-0.338321	0.462388	0.239599	0.098698	0.363787	...	0.277838	-0.110474	0.066928	0.128539	-0.189115	0.133558	-0.021053	149.62	0	0
1 rows × 32 columns

dftest0['pre_class']=reg.predict(dftest0.iloc[:,:-2])
dftest0.head(2)
Time	V1	V2	V3	V4	V5	V6	V7	V8	V9	...	V22	V23	V24	V25	V26	V27	V28	Amount	Class	pre_class
0	0.0	-1.359807	-0.072781	2.536347	1.378155	-0.338321	0.462388	0.239599	0.098698	0.363787	...	0.277838	-0.110474	0.066928	0.128539	-0.189115	0.133558	-0.021053	149.62	0	0
1	0.0	1.191857	0.266151	0.166480	0.448154	0.060018	-0.082361	-0.078803	0.085102	-0.255425	...	-0.638672	0.101288	-0.339846	0.167170	0.125895	-0.008983	0.014724	2.69	0	0
2 rows × 32 columns

dftest0.groupby(['Class','pre_class'])['Class'].count()
Class  pre_class
0      0            100
1      0             17
       1             83
Name: Class, dtype: int64
dftest0.to_csv("d:/d/creditcard.csv")