import numpy as np
ar=np.array([2,3,4,5,6,7,6])
ar1=np.array([3,4,1,6,8,3,9])
print(ar)
print(ar1)
[2 3 4 5 6 7 6]
[3 4 1 6 8 3 9]
print("Mean :",np.mean(ar))
print("Median :",np.median(ar))
print("Max :",np.max(ar))
print("Min :",np.min(ar))
print("Standard Deviation: ", np.std(ar))
Mean : 4.714285714285714
Median : 5.0
Max : 7
Min : 2
Standard Deviation:  1.6659862556700857
import statistics as sat
print("Mode  :", sat.mode(ar))
print("Range :", np.max(ar)-np.min(ar))
Mode  : 6
Range : 5
print("Correlation :",np.corrcoef(ar,ar1)[0,1])
Range : 0.4681044519385103