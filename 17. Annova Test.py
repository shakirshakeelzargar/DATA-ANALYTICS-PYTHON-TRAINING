import pandas as pd
df=pd.read_csv("annova.csv")
df
score	company
0	5	AirMobile
1	3	AirMobile
2	5	AirMobile
3	3	AirMobile
4	8	BingeTech
5	3	BingeTech
6	4	BingeTech
7	5	BingeTech
8	5	ComMobile
9	6	ComMobile
10	5	ComMobile
11	8	ComMobile
12	4	DataRoam
13	6	DataRoam
14	8	DataRoam
15	2	DataRoam
grps=pd.unique(df.company.values)
grps
array(['AirMobile', 'BingeTech', 'ComMobile', 'DataRoam'], dtype=object)
for grp in grps:
    print(grp)
AirMobile
BingeTech
ComMobile
DataRoam
d_data = {grp:df['score'][df.company == grp] for grp in grps}
d_data
{'AirMobile': 0    5
 1    3
 2    5
 3    3
 Name: score, dtype: int64, 'BingeTech': 4    8
 5    3
 6    4
 7    5
 Name: score, dtype: int64, 'ComMobile': 8     5
 9     6
 10    5
 11    8
 Name: score, dtype: int64, 'DataRoam': 12    4
 13    6
 14    8
 15    2
 Name: score, dtype: int64}
from scipy import stats
F, p = stats.f_oneway(d_data['AirMobile'], d_data['BingeTech'], 
                      d_data['ComMobile'],d_data['DataRoam'])
print(F)
print(p)
0.7272727272727273
0.5551086637384908