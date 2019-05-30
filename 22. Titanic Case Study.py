import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("d:/d/titanic/train.csv")
Age=pd.Series(df['Age'])
Age=Age.dropna()
df.head()
PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked
0	1	0	3	Braund, Mr. Owen Harris	male	22.0	1	0	A/5 21171	7.2500	NaN	S
1	2	1	1	Cumings, Mrs. John Bradley (Florence Briggs Th...	female	38.0	1	0	PC 17599	71.2833	C85	C
2	3	1	3	Heikkinen, Miss. Laina	female	26.0	0	0	STON/O2. 3101282	7.9250	NaN	S
3	4	1	1	Futrelle, Mrs. Jacques Heath (Lily May Peel)	female	35.0	1	0	113803	53.1000	C123	S
4	5	0	3	Allen, Mr. William Henry	male	35.0	0	0	373450	8.0500	NaN	S
y=df.describe()
y
PassengerId	Survived	Pclass	Age	SibSp	Parch	Fare
count	891.000000	891.000000	891.000000	714.000000	891.000000	891.000000	891.000000
mean	446.000000	0.383838	2.308642	29.699118	0.523008	0.381594	32.204208
std	257.353842	0.486592	0.836071	14.526497	1.102743	0.806057	49.693429
min	1.000000	0.000000	1.000000	0.420000	0.000000	0.000000	0.000000
25%	223.500000	0.000000	2.000000	20.125000	0.000000	0.000000	7.910400
50%	446.000000	0.000000	3.000000	28.000000	0.000000	0.000000	14.454200
75%	668.500000	1.000000	3.000000	38.000000	1.000000	0.000000	31.000000
max	891.000000	1.000000	3.000000	80.000000	8.000000	6.000000	512.329200
df.corr()
PassengerId	Survived	Pclass	Age	SibSp	Parch	Fare
PassengerId	1.000000	-0.005007	-0.035144	0.036847	-0.057527	-0.001652	0.012658
Survived	-0.005007	1.000000	-0.338481	-0.077221	-0.035322	0.081629	0.257307
Pclass	-0.035144	-0.338481	1.000000	-0.369226	0.083081	0.018443	-0.549500
Age	0.036847	-0.077221	-0.369226	1.000000	-0.308247	-0.189119	0.096067
SibSp	-0.057527	-0.035322	0.083081	-0.308247	1.000000	0.414838	0.159651
Parch	-0.001652	0.081629	0.018443	-0.189119	0.414838	1.000000	0.216225
Fare	0.012658	0.257307	-0.549500	0.096067	0.159651	0.216225	1.000000
df.describe(include=object)
Name	Sex	Ticket	Cabin	Embarked
count	891	891	891	204	889
unique	891	2	681	147	3
top	Salkjelsvik, Miss. Anna Kristine	male	1601	B96 B98	S
freq	1	577	7	4	644
plt.hist(Age)
(array([10.,  6., 32., 30., 40., 24., 23., 13.,  4.,  1.]),
 array([ 0.92 ,  8.828, 16.736, 24.644, 32.552, 40.46 , 48.368, 56.276,
        64.184, 72.092, 80.   ]),
 <a list of 10 Patch objects>)

f, ((ax1, ax2), (ax3, ax4))= plt.subplots(2,2)
ax1.hist(Age)
ax2.hist(df['SibSp'])
ax3.hist(df['Parch'])
ax4.hist(df['Fare'])
ax1.set_xlabel("Age")
ax1.set_ylabel("Count")
ax2.set_xlabel("SibSp")
ax2.set_ylabel("Count")
ax3.set_xlabel("Parch")
ax3.set_ylabel("Count")
ax4.set_xlabel("Fare")
ax4.set_ylabel("Count")
plt.show()

fs=plt.rcParams['figure.figsize']
#print(fs[0])
#print(fs[1])
fs[0]=10
fs[1]=7
plt.hist(df['Survived'])
Sur=pd.Series(df['Survived'])
Sur=Sur.replace(0,'No')
Sur=Sur.replace(1,'Yes')
Sur2=pd.DataFrame({'a':Sur})
x=Sur2.groupby('a')['a'].count()
print(x)
a
No     549
Yes    342
Name: a, dtype: int64
plt.bar(x.index.tolist(), x.values.tolist())
<BarContainer object of 2 artists>

pc=pd.Series(df['Pclass'])
pc=pc.replace(1,'1st')
pc=pc.replace(2,'2nd')
pc=pc.replace(3,'3rd')
pc2=pd.DataFrame({'a':pc})
xx=pc2.groupby('a')['a'].count()
print(xx)
a
1st    216
2nd    184
3rd    491
Name: a, dtype: int64
plt.bar(xx.index.tolist(), xx.values.tolist())
<BarContainer object of 3 artists>

sex=pd.Series(df['Sex'])
sex=sex.replace('male','MALE')
sex=sex.replace('female','FEMALE')
sex2=pd.DataFrame({'a':sex})
xxx=sex2.groupby('a')['a'].count()
print(xxx)
plt.bar(xxx.index.tolist(), xxx.values.tolist())
a
FEMALE    314
MALE      577
Name: a, dtype: int64
<BarContainer object of 2 artists>

emb=pd.Series(df['Embarked'])
emb=emb.replace('C','C1')
emb=emb.replace('Q','Q1')
emb=emb.replace('S','S1')
emb2=pd.DataFrame({'a':emb})
xxxx=emb2.groupby('a')['a'].count()
print(xxxx)
plt.bar(xxxx.index.tolist(), xxxx.values.tolist())
a
C1    168
Q1     77
S1    644
Name: a, dtype: int64
<BarContainer object of 3 artists>

f, ((ax1, ax2), (ax3, ax4))= plt.subplots(2,2)
ax1.bar(x.index.tolist(), x.values.tolist())
ax2.bar(xx.index.tolist(), xx.values.tolist())
ax3.bar(xxx.index.tolist(), xxx.values.tolist())
ax4.bar(xxxx.index.tolist(), xxxx.values.tolist())
ax1.set_xlabel("Survived")
ax1.set_ylabel("Count")
ax2.set_xlabel("Pclass")
ax2.set_ylabel("Count")
ax3.set_xlabel("Sex")
ax3.set_ylabel("Count")
ax4.set_xlabel("Embarked")
ax4.set_ylabel("Count")
plt.show()

df=pd.read_csv("d:/d/titanic/train.csv")
df.head()
PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked
0	1	0	3	Braund, Mr. Owen Harris	male	22.0	1	0	A/5 21171	7.2500	NaN	S
1	2	1	1	Cumings, Mrs. John Bradley (Florence Briggs Th...	female	38.0	1	0	PC 17599	71.2833	C85	C
2	3	1	3	Heikkinen, Miss. Laina	female	26.0	0	0	STON/O2. 3101282	7.9250	NaN	S
3	4	1	1	Futrelle, Mrs. Jacques Heath (Lily May Peel)	female	35.0	1	0	113803	53.1000	C123	S
4	5	0	3	Allen, Mr. William Henry	male	35.0	0	0	373450	8.0500	NaN	S
x=df['Age'].median()
x
28.0
df['Age'].fillna(28, inplace=True)
df['Embarked'].fillna('S', inplace=True)
df.corr()
PassengerId	Survived	Pclass	Age	SibSp	Parch	Fare
PassengerId	1.000000	-0.005007	-0.035144	0.034212	-0.057527	-0.001652	0.012658
Survived	-0.005007	1.000000	-0.338481	-0.064910	-0.035322	0.081629	0.257307
Pclass	-0.035144	-0.338481	1.000000	-0.339898	0.083081	0.018443	-0.549500
Age	0.034212	-0.064910	-0.339898	1.000000	-0.233296	-0.172482	0.096688
SibSp	-0.057527	-0.035322	0.083081	-0.233296	1.000000	0.414838	0.159651
Parch	-0.001652	0.081629	0.018443	-0.172482	0.414838	1.000000	0.216225
Fare	0.012658	0.257307	-0.549500	0.096688	0.159651	0.216225	1.000000
from sklearn import linear_model
reg=linear_model.LinearRegression()
reg.fit(df[['Pclass']],df['Fare'])
reg.score(df[['Pclass']],df['Fare'])
0.30194983231849915
df['Pre_Fare']=reg.predict(df[['Pclass']])
df['Var']=df['Fare']-df['Pre_Fare']
df
PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked	Pre_Fare	Var
0	1	0	3	Braund, Mr. Owen Harris	male	22.0	1	0	A/5 21171	7.2500	NaN	S	9.624097	-2.374097
1	2	1	1	Cumings, Mrs. John Bradley (Florence Briggs Th...	female	38.0	1	0	PC 17599	71.2833	C85	C	74.945133	-3.661833
2	3	1	3	Heikkinen, Miss. Laina	female	26.0	0	0	STON/O2. 3101282	7.9250	NaN	S	9.624097	-1.699097
3	4	1	1	Futrelle, Mrs. Jacques Heath (Lily May Peel)	female	35.0	1	0	113803	53.1000	C123	S	74.945133	-21.845133
4	5	0	3	Allen, Mr. William Henry	male	35.0	0	0	373450	8.0500	NaN	S	9.624097	-1.574097
5	6	0	3	Moran, Mr. James	male	28.0	0	0	330877	8.4583	NaN	Q	9.624097	-1.165797
6	7	0	1	McCarthy, Mr. Timothy J	male	54.0	0	0	17463	51.8625	E46	S	74.945133	-23.082633
7	8	0	3	Palsson, Master. Gosta Leonard	male	2.0	3	1	349909	21.0750	NaN	S	9.624097	11.450903
8	9	1	3	Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)	female	27.0	0	2	347742	11.1333	NaN	S	9.624097	1.509203
9	10	1	2	Nasser, Mrs. Nicholas (Adele Achem)	female	14.0	1	0	237736	30.0708	NaN	C	42.284615	-12.213815
10	11	1	3	Sandstrom, Miss. Marguerite Rut	female	4.0	1	1	PP 9549	16.7000	G6	S	9.624097	7.075903
11	12	1	1	Bonnell, Miss. Elizabeth	female	58.0	0	0	113783	26.5500	C103	S	74.945133	-48.395133
12	13	0	3	Saundercock, Mr. William Henry	male	20.0	0	0	A/5. 2151	8.0500	NaN	S	9.624097	-1.574097
13	14	0	3	Andersson, Mr. Anders Johan	male	39.0	1	5	347082	31.2750	NaN	S	9.624097	21.650903
14	15	0	3	Vestrom, Miss. Hulda Amanda Adolfina	female	14.0	0	0	350406	7.8542	NaN	S	9.624097	-1.769897
15	16	1	2	Hewlett, Mrs. (Mary D Kingcome)	female	55.0	0	0	248706	16.0000	NaN	S	42.284615	-26.284615
16	17	0	3	Rice, Master. Eugene	male	2.0	4	1	382652	29.1250	NaN	Q	9.624097	19.500903
17	18	1	2	Williams, Mr. Charles Eugene	male	28.0	0	0	244373	13.0000	NaN	S	42.284615	-29.284615
18	19	0	3	Vander Planke, Mrs. Julius (Emelia Maria Vande...	female	31.0	1	0	345763	18.0000	NaN	S	9.624097	8.375903
19	20	1	3	Masselmani, Mrs. Fatima	female	28.0	0	0	2649	7.2250	NaN	C	9.624097	-2.399097
20	21	0	2	Fynney, Mr. Joseph J	male	35.0	0	0	239865	26.0000	NaN	S	42.284615	-16.284615
21	22	1	2	Beesley, Mr. Lawrence	male	34.0	0	0	248698	13.0000	D56	S	42.284615	-29.284615
22	23	1	3	McGowan, Miss. Anna "Annie"	female	15.0	0	0	330923	8.0292	NaN	Q	9.624097	-1.594897
23	24	1	1	Sloper, Mr. William Thompson	male	28.0	0	0	113788	35.5000	A6	S	74.945133	-39.445133
24	25	0	3	Palsson, Miss. Torborg Danira	female	8.0	3	1	349909	21.0750	NaN	S	9.624097	11.450903
25	26	1	3	Asplund, Mrs. Carl Oscar (Selma Augusta Emilia...	female	38.0	1	5	347077	31.3875	NaN	S	9.624097	21.763403
26	27	0	3	Emir, Mr. Farred Chehab	male	28.0	0	0	2631	7.2250	NaN	C	9.624097	-2.399097
27	28	0	1	Fortune, Mr. Charles Alexander	male	19.0	3	2	19950	263.0000	C23 C25 C27	S	74.945133	188.054867
28	29	1	3	O'Dwyer, Miss. Ellen "Nellie"	female	28.0	0	0	330959	7.8792	NaN	Q	9.624097	-1.744897
29	30	0	3	Todoroff, Mr. Lalio	male	28.0	0	0	349216	7.8958	NaN	S	9.624097	-1.728297
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
861	862	0	2	Giles, Mr. Frederick Edward	male	21.0	1	0	28134	11.5000	NaN	S	42.284615	-30.784615
862	863	1	1	Swift, Mrs. Frederick Joel (Margaret Welles Ba...	female	48.0	0	0	17466	25.9292	D17	S	74.945133	-49.015933
863	864	0	3	Sage, Miss. Dorothy Edith "Dolly"	female	28.0	8	2	CA. 2343	69.5500	NaN	S	9.624097	59.925903
864	865	0	2	Gill, Mr. John William	male	24.0	0	0	233866	13.0000	NaN	S	42.284615	-29.284615
865	866	1	2	Bystrom, Mrs. (Karolina)	female	42.0	0	0	236852	13.0000	NaN	S	42.284615	-29.284615
866	867	1	2	Duran y More, Miss. Asuncion	female	27.0	1	0	SC/PARIS 2149	13.8583	NaN	C	42.284615	-28.426315
867	868	0	1	Roebling, Mr. Washington Augustus II	male	31.0	0	0	PC 17590	50.4958	A24	S	74.945133	-24.449333
868	869	0	3	van Melkebeke, Mr. Philemon	male	28.0	0	0	345777	9.5000	NaN	S	9.624097	-0.124097
869	870	1	3	Johnson, Master. Harold Theodor	male	4.0	1	1	347742	11.1333	NaN	S	9.624097	1.509203
870	871	0	3	Balkic, Mr. Cerin	male	26.0	0	0	349248	7.8958	NaN	S	9.624097	-1.728297
871	872	1	1	Beckwith, Mrs. Richard Leonard (Sallie Monypeny)	female	47.0	1	1	11751	52.5542	D35	S	74.945133	-22.390933
872	873	0	1	Carlsson, Mr. Frans Olof	male	33.0	0	0	695	5.0000	B51 B53 B55	S	74.945133	-69.945133
873	874	0	3	Vander Cruyssen, Mr. Victor	male	47.0	0	0	345765	9.0000	NaN	S	9.624097	-0.624097
874	875	1	2	Abelson, Mrs. Samuel (Hannah Wizosky)	female	28.0	1	0	P/PP 3381	24.0000	NaN	C	42.284615	-18.284615
875	876	1	3	Najib, Miss. Adele Kiamie "Jane"	female	15.0	0	0	2667	7.2250	NaN	C	9.624097	-2.399097
876	877	0	3	Gustafsson, Mr. Alfred Ossian	male	20.0	0	0	7534	9.8458	NaN	S	9.624097	0.221703
877	878	0	3	Petroff, Mr. Nedelio	male	19.0	0	0	349212	7.8958	NaN	S	9.624097	-1.728297
878	879	0	3	Laleff, Mr. Kristo	male	28.0	0	0	349217	7.8958	NaN	S	9.624097	-1.728297
879	880	1	1	Potter, Mrs. Thomas Jr (Lily Alexenia Wilson)	female	56.0	0	1	11767	83.1583	C50	C	74.945133	8.213167
880	881	1	2	Shelley, Mrs. William (Imanita Parrish Hall)	female	25.0	0	1	230433	26.0000	NaN	S	42.284615	-16.284615
881	882	0	3	Markun, Mr. Johann	male	33.0	0	0	349257	7.8958	NaN	S	9.624097	-1.728297
882	883	0	3	Dahlberg, Miss. Gerda Ulrika	female	22.0	0	0	7552	10.5167	NaN	S	9.624097	0.892603
883	884	0	2	Banfield, Mr. Frederick James	male	28.0	0	0	C.A./SOTON 34068	10.5000	NaN	S	42.284615	-31.784615
884	885	0	3	Sutehall, Mr. Henry Jr	male	25.0	0	0	SOTON/OQ 392076	7.0500	NaN	S	9.624097	-2.574097
885	886	0	3	Rice, Mrs. William (Margaret Norton)	female	39.0	0	5	382652	29.1250	NaN	Q	9.624097	19.500903
886	887	0	2	Montvila, Rev. Juozas	male	27.0	0	0	211536	13.0000	NaN	S	42.284615	-29.284615
887	888	1	1	Graham, Miss. Margaret Edith	female	19.0	0	0	112053	30.0000	B42	S	74.945133	-44.945133
888	889	0	3	Johnston, Miss. Catherine Helen "Carrie"	female	28.0	1	2	W./C. 6607	23.4500	NaN	S	9.624097	13.825903
889	890	1	1	Behr, Mr. Karl Howell	male	26.0	0	0	111369	30.0000	C148	C	74.945133	-44.945133
890	891	0	3	Dooley, Mr. Patrick	male	32.0	0	0	370376	7.7500	NaN	Q	9.624097	-1.874097
891 rows × 14 columns

df.corr()
PassengerId	Survived	Pclass	Age	SibSp	Parch	Fare	Pre_Fare	Var
PassengerId	1.000000	-0.005007	-3.514399e-02	0.034212	-0.057527	-0.001652	0.012658	3.514399e-02	-7.963423e-03
Survived	-0.005007	1.000000	-3.384810e-01	-0.064910	-0.035322	0.081629	0.257307	3.384810e-01	8.535229e-02
Pclass	-0.035144	-0.338481	1.000000e+00	-0.339898	0.083081	0.018443	-0.549500	-1.000000e+00	-4.609707e-16
Age	0.034212	-0.064910	-3.398983e-01	1.000000	-0.233296	-0.172482	0.096688	3.398983e-01	-1.078231e-01
SibSp	-0.057527	-0.035322	8.308136e-02	-0.233296	1.000000	0.414838	0.159651	-8.308136e-02	2.457280e-01
Parch	-0.001652	0.081629	1.844267e-02	-0.172482	0.414838	1.000000	0.216225	-1.844267e-02	2.709286e-01
Fare	0.012658	0.257307	-5.494996e-01	0.096688	0.159651	0.216225	1.000000	5.494996e-01	8.354940e-01
Pre_Fare	0.035144	0.338481	-1.000000e+00	0.339898	-0.083081	-0.018443	0.549500	1.000000e+00	5.046457e-16
Var	-0.007963	0.085352	-4.609707e-16	-0.107823	0.245728	0.270929	0.835494	5.046457e-16	1.000000e+00
dfinput=df['Pclass']
dfoutput=df['Survived']
from sklearn import linear_model
reg=linear_model.LogisticRegression()
reg.fit(df[['Pclass']], dfoutput)
reg.score(df[['Pclass']], dfoutput)
0.6790123456790124
df['pre_survival']=reg.predict(df[['Pclass']])
df
PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked	Pre_Fare	Var	pre_survival
0	1	0	3	Braund, Mr. Owen Harris	male	22.0	1	0	A/5 21171	7.2500	NaN	S	9.624097	-2.374097	0
1	2	1	1	Cumings, Mrs. John Bradley (Florence Briggs Th...	female	38.0	1	0	PC 17599	71.2833	C85	C	74.945133	-3.661833	1
2	3	1	3	Heikkinen, Miss. Laina	female	26.0	0	0	STON/O2. 3101282	7.9250	NaN	S	9.624097	-1.699097	0
3	4	1	1	Futrelle, Mrs. Jacques Heath (Lily May Peel)	female	35.0	1	0	113803	53.1000	C123	S	74.945133	-21.845133	1
4	5	0	3	Allen, Mr. William Henry	male	35.0	0	0	373450	8.0500	NaN	S	9.624097	-1.574097	0
5	6	0	3	Moran, Mr. James	male	28.0	0	0	330877	8.4583	NaN	Q	9.624097	-1.165797	0
6	7	0	1	McCarthy, Mr. Timothy J	male	54.0	0	0	17463	51.8625	E46	S	74.945133	-23.082633	1
7	8	0	3	Palsson, Master. Gosta Leonard	male	2.0	3	1	349909	21.0750	NaN	S	9.624097	11.450903	0
8	9	1	3	Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)	female	27.0	0	2	347742	11.1333	NaN	S	9.624097	1.509203	0
9	10	1	2	Nasser, Mrs. Nicholas (Adele Achem)	female	14.0	1	0	237736	30.0708	NaN	C	42.284615	-12.213815	0
10	11	1	3	Sandstrom, Miss. Marguerite Rut	female	4.0	1	1	PP 9549	16.7000	G6	S	9.624097	7.075903	0
11	12	1	1	Bonnell, Miss. Elizabeth	female	58.0	0	0	113783	26.5500	C103	S	74.945133	-48.395133	1
12	13	0	3	Saundercock, Mr. William Henry	male	20.0	0	0	A/5. 2151	8.0500	NaN	S	9.624097	-1.574097	0
13	14	0	3	Andersson, Mr. Anders Johan	male	39.0	1	5	347082	31.2750	NaN	S	9.624097	21.650903	0
14	15	0	3	Vestrom, Miss. Hulda Amanda Adolfina	female	14.0	0	0	350406	7.8542	NaN	S	9.624097	-1.769897	0
15	16	1	2	Hewlett, Mrs. (Mary D Kingcome)	female	55.0	0	0	248706	16.0000	NaN	S	42.284615	-26.284615	0
16	17	0	3	Rice, Master. Eugene	male	2.0	4	1	382652	29.1250	NaN	Q	9.624097	19.500903	0
17	18	1	2	Williams, Mr. Charles Eugene	male	28.0	0	0	244373	13.0000	NaN	S	42.284615	-29.284615	0
18	19	0	3	Vander Planke, Mrs. Julius (Emelia Maria Vande...	female	31.0	1	0	345763	18.0000	NaN	S	9.624097	8.375903	0
19	20	1	3	Masselmani, Mrs. Fatima	female	28.0	0	0	2649	7.2250	NaN	C	9.624097	-2.399097	0
20	21	0	2	Fynney, Mr. Joseph J	male	35.0	0	0	239865	26.0000	NaN	S	42.284615	-16.284615	0
21	22	1	2	Beesley, Mr. Lawrence	male	34.0	0	0	248698	13.0000	D56	S	42.284615	-29.284615	0
22	23	1	3	McGowan, Miss. Anna "Annie"	female	15.0	0	0	330923	8.0292	NaN	Q	9.624097	-1.594897	0
23	24	1	1	Sloper, Mr. William Thompson	male	28.0	0	0	113788	35.5000	A6	S	74.945133	-39.445133	1
24	25	0	3	Palsson, Miss. Torborg Danira	female	8.0	3	1	349909	21.0750	NaN	S	9.624097	11.450903	0
25	26	1	3	Asplund, Mrs. Carl Oscar (Selma Augusta Emilia...	female	38.0	1	5	347077	31.3875	NaN	S	9.624097	21.763403	0
26	27	0	3	Emir, Mr. Farred Chehab	male	28.0	0	0	2631	7.2250	NaN	C	9.624097	-2.399097	0
27	28	0	1	Fortune, Mr. Charles Alexander	male	19.0	3	2	19950	263.0000	C23 C25 C27	S	74.945133	188.054867	1
28	29	1	3	O'Dwyer, Miss. Ellen "Nellie"	female	28.0	0	0	330959	7.8792	NaN	Q	9.624097	-1.744897	0
29	30	0	3	Todoroff, Mr. Lalio	male	28.0	0	0	349216	7.8958	NaN	S	9.624097	-1.728297	0
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
861	862	0	2	Giles, Mr. Frederick Edward	male	21.0	1	0	28134	11.5000	NaN	S	42.284615	-30.784615	0
862	863	1	1	Swift, Mrs. Frederick Joel (Margaret Welles Ba...	female	48.0	0	0	17466	25.9292	D17	S	74.945133	-49.015933	1
863	864	0	3	Sage, Miss. Dorothy Edith "Dolly"	female	28.0	8	2	CA. 2343	69.5500	NaN	S	9.624097	59.925903	0
864	865	0	2	Gill, Mr. John William	male	24.0	0	0	233866	13.0000	NaN	S	42.284615	-29.284615	0
865	866	1	2	Bystrom, Mrs. (Karolina)	female	42.0	0	0	236852	13.0000	NaN	S	42.284615	-29.284615	0
866	867	1	2	Duran y More, Miss. Asuncion	female	27.0	1	0	SC/PARIS 2149	13.8583	NaN	C	42.284615	-28.426315	0
867	868	0	1	Roebling, Mr. Washington Augustus II	male	31.0	0	0	PC 17590	50.4958	A24	S	74.945133	-24.449333	1
868	869	0	3	van Melkebeke, Mr. Philemon	male	28.0	0	0	345777	9.5000	NaN	S	9.624097	-0.124097	0
869	870	1	3	Johnson, Master. Harold Theodor	male	4.0	1	1	347742	11.1333	NaN	S	9.624097	1.509203	0
870	871	0	3	Balkic, Mr. Cerin	male	26.0	0	0	349248	7.8958	NaN	S	9.624097	-1.728297	0
871	872	1	1	Beckwith, Mrs. Richard Leonard (Sallie Monypeny)	female	47.0	1	1	11751	52.5542	D35	S	74.945133	-22.390933	1
872	873	0	1	Carlsson, Mr. Frans Olof	male	33.0	0	0	695	5.0000	B51 B53 B55	S	74.945133	-69.945133	1
873	874	0	3	Vander Cruyssen, Mr. Victor	male	47.0	0	0	345765	9.0000	NaN	S	9.624097	-0.624097	0
874	875	1	2	Abelson, Mrs. Samuel (Hannah Wizosky)	female	28.0	1	0	P/PP 3381	24.0000	NaN	C	42.284615	-18.284615	0
875	876	1	3	Najib, Miss. Adele Kiamie "Jane"	female	15.0	0	0	2667	7.2250	NaN	C	9.624097	-2.399097	0
876	877	0	3	Gustafsson, Mr. Alfred Ossian	male	20.0	0	0	7534	9.8458	NaN	S	9.624097	0.221703	0
877	878	0	3	Petroff, Mr. Nedelio	male	19.0	0	0	349212	7.8958	NaN	S	9.624097	-1.728297	0
878	879	0	3	Laleff, Mr. Kristo	male	28.0	0	0	349217	7.8958	NaN	S	9.624097	-1.728297	0
879	880	1	1	Potter, Mrs. Thomas Jr (Lily Alexenia Wilson)	female	56.0	0	1	11767	83.1583	C50	C	74.945133	8.213167	1
880	881	1	2	Shelley, Mrs. William (Imanita Parrish Hall)	female	25.0	0	1	230433	26.0000	NaN	S	42.284615	-16.284615	0
881	882	0	3	Markun, Mr. Johann	male	33.0	0	0	349257	7.8958	NaN	S	9.624097	-1.728297	0
882	883	0	3	Dahlberg, Miss. Gerda Ulrika	female	22.0	0	0	7552	10.5167	NaN	S	9.624097	0.892603	0
883	884	0	2	Banfield, Mr. Frederick James	male	28.0	0	0	C.A./SOTON 34068	10.5000	NaN	S	42.284615	-31.784615	0
884	885	0	3	Sutehall, Mr. Henry Jr	male	25.0	0	0	SOTON/OQ 392076	7.0500	NaN	S	9.624097	-2.574097	0
885	886	0	3	Rice, Mrs. William (Margaret Norton)	female	39.0	0	5	382652	29.1250	NaN	Q	9.624097	19.500903	0
886	887	0	2	Montvila, Rev. Juozas	male	27.0	0	0	211536	13.0000	NaN	S	42.284615	-29.284615	0
887	888	1	1	Graham, Miss. Margaret Edith	female	19.0	0	0	112053	30.0000	B42	S	74.945133	-44.945133	1
888	889	0	3	Johnston, Miss. Catherine Helen "Carrie"	female	28.0	1	2	W./C. 6607	23.4500	NaN	S	9.624097	13.825903	0
889	890	1	1	Behr, Mr. Karl Howell	male	26.0	0	0	111369	30.0000	C148	C	74.945133	-44.945133	1
890	891	0	3	Dooley, Mr. Patrick	male	32.0	0	0	370376	7.7500	NaN	Q	9.624097	-1.874097	0
891 rows × 15 columns