import numpy as np

a1 = [6, 4, 5, 10]
a2 = [8, 5, 3, 3]
a3 = [5, 4, 8, 4]
a4 = [4, 11, 7, 13]
a5 = [5, 8, 7, 6]
a6 = [7, 3, 5, 9]

dice = np.array([a1, a2, a3, a4, a5, a6])
dice
array([[ 6,  4,  5, 10],
       [ 8,  5,  3,  3],
       [ 5,  4,  8,  4],
       [ 4, 11,  7, 13],
       [ 5,  8,  7,  6],
       [ 7,  3,  5,  9]])
In this instance:

Rows = 6 [die rolls 1–6]

Columns = 4 [samples]

So we take (6–1) and multiply by (4–1) to get 15 degrees of freedom. Critical Chi-Square Values is 24.9958

chi2_stat, p_val, dof, ex = stats.chi2_contingency(dice)

print("===Chi2 Stat===")
print(chi2_stat)
print("\n")

print("===Degrees of Freedom===")
print(dof)
print("\n")

print("===P-Value===")
print(p_val)
print("\n")
===Chi2 Stat===
16.490612061288754


===Degrees of Freedom===
15


===P-Value===
0.35021521809742745

