import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset('tips')
tips.shape
tips.head(1)
total_bill	tip	sex	smoker	day	time	size
0	16.99	1.01	Female	No	Sun	Dinner	2
#histogram
#sns.distplot(tips['total_bill'], kde=True) #density plot
#sns.distplot(tips['total_bill'], kde=False) #without density plot
#sns.distplot(tips['total_bill'], hist=False) #without density plot
sns.distplot(tips['total_bill'], rug=False)
C:\Users\Rajinder\Anaconda3\lib\site-packages\matplotlib\axes\_axes.py:6462: UserWarning: The 'normed' kwarg is deprecated, and has been replaced by the 'density' kwarg.
  warnings.warn("The 'normed' kwarg is deprecated, and has been "
<matplotlib.axes._subplots.AxesSubplot at 0x2207a54c160>

sns.countplot('day',data=tips)
C:\Users\Rajinder\Anaconda3\lib\site-packages\seaborn\categorical.py:1460: FutureWarning: remove_na is deprecated and is a private function. Do not use.
  stat_data = remove_na(group_data)
<matplotlib.axes._subplots.AxesSubplot at 0x2207a5a66a0>

#bivariate Data
#scatter
sns.regplot(x='total_bill',y='tip', data=tips)
<matplotlib.axes._subplots.AxesSubplot at 0x2207a658b70>

sc, ax=plt.subplots()
ax=sns.regplot(x='total_bill',y='tip', data=tips)
ax.set_title('Scatter Plot')
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tips")
plt.show()

#sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
sns.jointplot(x='total_bill', y='tip', data=tips)
<seaborn.axisgrid.JointGrid at 0x19921f932e8>

sns.kdeplot(data=tips['total_bill'],
           data2=tips['tip'],
           shade=True)
<matplotlib.axes._subplots.AxesSubplot at 0x19921e6be10>

#bar plot
sns.barplot(x='time',y='total_bill', data=tips)
C:\Users\Rajinder\Anaconda3\lib\site-packages\seaborn\categorical.py:1460: FutureWarning: remove_na is deprecated and is a private function. Do not use.
  stat_data = remove_na(group_data)
<matplotlib.axes._subplots.AxesSubplot at 0x199231193c8>

sns.boxplot(x='time',y='total_bill', data=tips)
C:\Users\Rajinder\Anaconda3\lib\site-packages\seaborn\categorical.py:462: FutureWarning: remove_na is deprecated and is a private function. Do not use.
  box_data = remove_na(group_data)
<matplotlib.axes._subplots.AxesSubplot at 0x19923190668>

sns.violinplot(x='time',y='total_bill', data=tips)
C:\Users\Rajinder\Anaconda3\lib\site-packages\seaborn\categorical.py:598: FutureWarning: remove_na is deprecated and is a private function. Do not use.
  kde_data = remove_na(group_data)
C:\Users\Rajinder\Anaconda3\lib\site-packages\seaborn\categorical.py:826: FutureWarning: remove_na is deprecated and is a private function. Do not use.
  violin_data = remove_na(group_data)
<matplotlib.axes._subplots.AxesSubplot at 0x19923215cf8>

sns.pairplot(tips)
<seaborn.axisgrid.PairGrid at 0x1992525ac88>

sns.violinplot(x='time',y='total_bill', data=tips,
               hue='sex', split=True)
C:\Users\Rajinder\Anaconda3\lib\site-packages\seaborn\categorical.py:647: FutureWarning: remove_na is deprecated and is a private function. Do not use.
  kde_data = remove_na(group_data[hue_mask])
C:\Users\Rajinder\Anaconda3\lib\site-packages\seaborn\categorical.py:895: FutureWarning: remove_na is deprecated and is a private function. Do not use.
  violin_data = remove_na(group_data[hue_mask])
C:\Users\Rajinder\Anaconda3\lib\site-packages\seaborn\categorical.py:915: FutureWarning: remove_na is deprecated and is a private function. Do not use.
  violin_data = remove_na(group_data)
<matplotlib.axes._subplots.AxesSubplot at 0x19925897e10>

#fit_reg=False to hide regression line
sns.lmplot(x='total_bill',y='tip', data=tips,
           fit_reg=False,
           hue='sex',
           scatter_kws={'s':tips['size']*30}
          )
<seaborn.axisgrid.FacetGrid at 0x19926b2a278>

sns.lmplot(x='total_bill',y='tip', data=tips,
           fit_reg=False,
           hue='sex',
           scatter_kws={'s':tips['size']*30},
           markers=['o','x']
          )
<seaborn.axisgrid.FacetGrid at 0x19926c650b8>

anscombe= sns.load_dataset('anscombe')
sns.lmplot(x='x', y='y', data=anscombe,
          fit_reg=False,
          col='dataset', col_wrap=2)
<seaborn.axisgrid.FacetGrid at 0x19926f9aa58>
