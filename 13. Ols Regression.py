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
#step-1 => get the correlation
df.corr()
Sales	Mark_Exp	Hr_Cost
Sales	1.000000	0.957436	0.420084
Mark_Exp	0.957436	1.000000	0.402204
Hr_Cost	0.420084	0.402204	1.000000
import statsmodels.formula.api as smf
md=smf.ols(formula="Sales~Mark_Exp",data=df) #ordinary least square
reg=md.fit() #learning phase for algo.
reg.summary()
#reg.params
C:\Users\Rajinder\AppData\Roaming\Python\Python36\site-packages\scipy\stats\stats.py:1390: UserWarning: kurtosistest only valid for n>=20 ... continuing anyway, n=8
  "anyway, n=%i" % int(n))
OLS Regression Results
Dep. Variable:	Sales	R-squared:	0.917
Model:	OLS	Adj. R-squared:	0.903
Method:	Least Squares	F-statistic:	66.01
Date:	Mon, 28 Jan 2019	Prob (F-statistic):	0.000187
Time:	11:57:31	Log-Likelihood:	-26.465
No. Observations:	8	AIC:	56.93
Df Residuals:	6	BIC:	57.09
Df Model:	1		
Covariance Type:	nonrobust		
coef	std err	t	P>|t|	[0.025	0.975]
Intercept	32.0524	12.955	2.474	0.048	0.353	63.752
Mark_Exp	6.6958	0.824	8.125	0.000	4.679	8.712
Omnibus:	0.586	Durbin-Watson:	2.272
Prob(Omnibus):	0.746	Jarque-Bera (JB):	0.210
Skew:	-0.337	Prob(JB):	0.900
Kurtosis:	2.579	Cond. No.	75.7
df['Pre_Sales']=6.6958*df['Mark_Exp']+32.052402
df['Var']=df['Sales']-df['Pre_Sales']
df
Sales	Mark_Exp	Hr_Cost	Pre_Sales	Var
0	100	10	20	99.010402	0.989598
1	110	11	22	105.706202	4.293798
2	120	15	21	132.489402	-12.489402
3	130	14	22	125.793602	4.206398
4	140	17	23	145.881002	-5.881002
5	150	18	24	152.576802	-2.576802
6	160	19	20	159.272602	0.727398
7	170	19	23	159.272602	10.727398
def getsales(exp):
    return 6.6958*exp+32.052402
expense=16
sal=getsales(expense)
print("Sales for 16 Expense ",sal)
print("Seles for 26 is ",getsales(26))
Sales for 16 Expense  139.185202
Seles for 26 is  206.143202
lsexp=[20,20.5,21]
lssales=[]
for a in lsexp:
    lssales.append(getsales(a))
print("Expense :", lsexp)
print("Sales :", lssales)
Expense : [20, 20.5, 21]
Sales : [165.968402, 169.316302, 172.66420200000002]
import matplotlib.pyplot as plt
plt.scatter(df['Mark_Exp'],df['Sales'], color='k', label='Existing Data')
plt.plot(df['Mark_Exp'],df['Pre_Sales'], color='r', label='Reg Line')
plt.scatter(16,getsales(16), s=100, color='green')
plt.scatter(20,getsales(20), s=100, color='green')
plt.plot(lsexp, lssales, color='b', label='Predicted Line')
plt.xlabel("Marketing Expenses")
plt.ylabel("Sales in INR")
plt.legend()
plt.show()

import statsmodels.formula.api as smf
md=smf.ols(formula="Sales~Mark_Exp+Hr_Cost",data=df) #ordinary least square
reg=md.fit() #learning phase for algo.
reg.summary()
C:\Users\Rajinder\AppData\Roaming\Python\Python36\site-packages\scipy\stats\stats.py:1390: UserWarning: kurtosistest only valid for n>=20 ... continuing anyway, n=8
  "anyway, n=%i" % int(n))
OLS Regression Results
Dep. Variable:	Sales	R-squared:	0.918
Model:	OLS	Adj. R-squared:	0.885
Method:	Least Squares	F-statistic:	28.04
Date:	Mon, 28 Jan 2019	Prob (F-statistic):	0.00192
Time:	12:14:17	Log-Likelihood:	-26.394
No. Observations:	8	AIC:	58.79
Df Residuals:	5	BIC:	59.03
Df Model:	2		
Covariance Type:	nonrobust		
coef	std err	t	P>|t|	[0.025	0.975]
Intercept	18.5104	47.458	0.390	0.713	-103.483	140.504
Mark_Exp	6.5783	0.977	6.731	0.001	4.066	9.091
Hr_Cost	0.7016	2.348	0.299	0.777	-5.335	6.738
Omnibus:	0.353	Durbin-Watson:	2.086
Prob(Omnibus):	0.838	Jarque-Bera (JB):	0.315
Skew:	-0.343	Prob(JB):	0.854
Kurtosis:	2.312	Cond. No.	436.
df['Pre_Sales1']= 6.5783*df['Mark_Exp']+0.7016*df['Hr_Cost']+18.5104
df['Var1']=df['Sales']-df['Pre_Sales1']
df
Sales	Mark_Exp	Hr_Cost	Pre_Sales	Var	Pre_Sales1	Var1
0	100	10	20	99.010402	0.989598	98.3254	1.6746
1	110	11	22	105.706202	4.293798	106.3069	3.6931
2	120	15	21	132.489402	-12.489402	131.9185	-11.9185
3	130	14	22	125.793602	4.206398	126.0418	3.9582
4	140	17	23	145.881002	-5.881002	146.4783	-6.4783
5	150	18	24	152.576802	-2.576802	153.7582	-3.7582
6	160	19	20	159.272602	0.727398	157.5301	2.4699
7	170	19	23	159.272602	10.727398	159.6349	10.3651