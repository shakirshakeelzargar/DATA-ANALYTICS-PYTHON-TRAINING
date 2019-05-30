import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
tips=sns.load_dataset('tips')
tips.shape
tips.head(2)
total_bill	tip	sex	smoker	day	time	size
0	16.99	1.01	Female	No	Sun	Dinner	2
1	10.34	1.66	Male	No	Sun	Dinner	3
#histogram
tips['total_bill'].plot.hist()
#tips.plot.hist(by='total_bill')
<matplotlib.axes._subplots.AxesSubplot at 0x1fe55ac9240>

tips['tip'].plot.kde()
<matplotlib.axes._subplots.AxesSubplot at 0x1fe4fc68f28>

tips.plot.scatter(x='total_bill',y='tip',c='r',s=100)
<matplotlib.axes._subplots.AxesSubplot at 0x1fe57858668>

tips.dtypes
total_bill     float64
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
dtype: object
tips[0:10].plot.bar(x='smoker',y='total_bill')
<matplotlib.axes._subplots.AxesSubplot at 0x1fe524fa630>

tips.plot.line(x='time',y='total_bill')
<matplotlib.axes._subplots.AxesSubplot at 0x1fe5299a0f0>

tips.plot.area(x='time',y='total_bill')
<matplotlib.axes._subplots.AxesSubplot at 0x1fe52aad0f0>

tips[0:10].plot.barh(x='smoker',y='total_bill')
<matplotlib.axes._subplots.AxesSubplot at 0x1fe53581828>

tips.plot.density(x='total_bill')
<matplotlib.axes._subplots.AxesSubplot at 0x1fe539714a8>

sr=tips.groupby('smoker')['total_bill'].sum()

smokedf=pd.DataFrame({'Smoker':sr.index.tolist(),
                      'Total_Sales':sr.values.tolist()})
smokedf
Smoker	Total_Sales
0	Yes	1930.34
1	No	2897.43
smokedf.plot.pie(y='Total_Sales',x='Smoker')
<matplotlib.axes._subplots.AxesSubplot at 0x1fe55174fd0>

#hexbin plot
#tips.plot.hexbin(x='total_bill', y='tip')
tips.plot.hexbin(x='total_bill', y='tip', gridsize=10)
<matplotlib.axes._subplots.AxesSubplot at 0x1fe578b6cc0>

f,ax =plt.subplots()
#hexbin plot
ax=tips.plot.hexbin(x='total_bill', y='tip',ax=ax)
plt.show()
