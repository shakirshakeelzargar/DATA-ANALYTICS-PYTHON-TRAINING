import pandas as pd
df=pd.read_excel("LoanDataSet_v1.xlsx")
df.head()
id	loan_amnt	funded_amnt	funded_amnt_inv	term	int_rate	installment	grade	sub_grade	emp_length	...	recoveries	collection_recovery_fee	last_pymnt_d	last_pymnt_amnt	next_pymnt_d	last_credit_pull_d	collections_12_mths_ex_med	mths_since_last_major_derog	policy_code	application_type
0	1	5000	5000	4975.0	36 months	0.1065	162.87	B	B2	10+ years	...	0.0	0.00	2015-01-01	171.62	NaN	2018-09-01	0	NaN	1	Individual
1	2	2500	2500	2500.0	60 months	0.1527	59.83	C	C4	< 1 year	...	122.9	1.11	2013-04-01	119.66	NaN	2016-10-01	0	NaN	1	Individual
2	3	2400	2400	2400.0	36 months	0.1596	84.33	C	C5	10+ years	...	0.0	0.00	2014-06-01	649.91	NaN	2017-06-01	0	NaN	1	Individual
3	4	10000	10000	10000.0	36 months	0.1349	339.31	C	C1	10+ years	...	0.0	0.00	2015-01-01	357.48	NaN	2016-04-01	0	NaN	1	Individual
4	5	3000	3000	3000.0	60 months	0.1269	67.79	B	B5	1 year	...	0.0	0.00	2017-01-01	67.30	NaN	2018-04-01	0	NaN	1	Individual
5 rows × 39 columns

d={'grade':{'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7}}                                 
df.replace(d, inplace=True)
print(df['purpose'].dtype)
df["new_purpose"] = df["purpose"].astype('category')
df1["new_purpose"] = df1["new_purpose"].cat.codes
print(df['new_purpose'].dtype)
df['new_purpose'].value_counts()
object
category
debt_consolidation    5155
credit_card           1503
other                  865
home_improvement       630
small_business         439
major_purchase         365
car                    298
wedding                217
medical                176
moving                 126
house                  113
vacation                91
renewable_energy        22
Name: new_purpose, dtype: int64
import numpy as  np
print(df['purpose'].value_counts())
df['A_purpose']=np.where(df["purpose"].str.contains("wedding"),1,0)
print(df['A_purpose'].value_counts())
debt_consolidation    5155
credit_card           1503
other                  865
home_improvement       630
small_business         439
major_purchase         365
car                    298
wedding                217
medical                176
moving                 126
house                  113
vacation                91
renewable_energy        22
Name: purpose, dtype: int64
0    9783
1     217
Name: A_purpose, dtype: int64
from sklearn.preprocessing import LabelEncoder
lb_make = LabelEncoder()
df["B_Purpose"] = lb_make.fit_transform(df["purpose"])
print(df['B_Purpose'].value_counts())
2     5155
1     1503
8      865
3      630
10     439
5      365
0      298
12     217
6      176
7      126
4      113
11      91
9       22
Name: B_Purpose, dtype: int64
import pandas as pd
headers = ["symboling", "normalized_losses", "make", "fuel_type", "aspiration",
           "num_doors", "body_style", "drive_wheels", "engine_location",
           "wheel_base", "length", "width", "height", "curb_weight",
           "engine_type", "num_cylinders", "engine_size", "fuel_system",
           "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
           "city_mpg", "highway_mpg", "price"]

df=pd.read_csv("imports-80.data",  
               header=None, 
               names=headers,
              na_values="?")
df1=df.select_dtypes(include=['object']).copy()
df2=df1[df1.isnull().any(axis=1)]
print(df1.shape)
df1=df1.drop(df2.index.tolist())
print(df1.shape)