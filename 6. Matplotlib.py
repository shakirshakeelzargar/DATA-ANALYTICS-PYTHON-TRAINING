import matplotlib.pyplot as plt
lx=[1,2,3,4,5,6]
ly=[10,12,18,5,4,6]

lx1=[1,3,5,7,9,11]
lx2=[2,4,6,8,10,12]
ly1=[10,12,18,5,4,6]
ly2=[4,6,7,15,9,12]
lx1=lx[ly.index(max(ly))]
ly1=max(ly)
print(lx1, ly1)
3 18
plt.bar(lx, ly1, color='red', label='Product A Sales')
plt.bar(lx, ly2, color='green', label='Product B Sales',
       alpha=.5)
plt.ylim(2,30)
plt.legend(loc=2)
plt.show()

plt.bar(lx1, ly1, color='red', label='Product A Sales')
plt.bar(lx2, ly2, color='green', label='Product B Sales',
       alpha=.5)
plt.ylim(2,30)
plt.legend(loc=2)
plt.show()

plt.bar(lx, ly, color='r', label='Total Sales')
plt.legend(loc=2)
plt.xlabel("Nos of Weeks")
plt.ylabel("Sales Amount")
plt.title("Weekly Sales Report")
plt.ylim(2,20)
for i in range(len(lx)):
     plt.annotate(xy=[lx[i],ly[i]+.5],s=ly[i])  

plt.annotate(xy=[lx[ly.index(max(ly))]+.5, max(ly)+.5],
             s="<-Highest Sales",
            color='green')
plt.show()

print(lx1)
print(lx2)
print(ly1)
print(ly2)
[1, 3, 5, 7, 9, 11]
[2, 4, 6, 8, 10, 12]
[10, 12, 18, 5, 4, 6]
[4, 6, 7, 15, 9, 12]
plt.plot(lx1, ly1, label='Product A Sales')
plt.bar(lx2, ly2, label='Product A Profit', color='red')
plt.legend()
plt.show()

plt.scatter(lx1, ly1, label='Product A Sales',
           marker='+', s=50, color='red')
plt.scatter(lx2, ly2, label='Product B Sales'
           , s=50, color='blue')
plt.legend()
plt.show()

lb=['Math','Science','Physics', 'Chem']
ls=[15,66,56,78]
plt.pie(ls, labels=lb, shadow=True,
       startangle=90,explode=(0,0.2,0,0),
       colors=['green','blue','red','black'])
plt.show()

ls=[1,2,3,4,5,6,7,8,9,10,-49,80]
plt.boxplot(ls)
plt.show()

f=open("d:/d/graphfile.csv")
ls=f.readlines()
lx=[]
ly=[]
ly1=[]
ly2=[]
for a in ls[1:]:
    rw=a.split(',')
    lx.append(int(rw[0]))
    ly.append(int(rw[1]))
    ly1.append(int(rw[2]))
    ly2.append(int(rw[3]))
print(lx)
print(ly)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]
[1, 4, 3, 4, 1, 4, 1, 4, 3, 1, 3, 1, 1, 1, 1, 1, 4, 2, 1, 3, 2, 2, 4, 4, 4, 3, 3, 2, 3, 4, 2, 4, 2, 4, 4, 3, 4, 4, 4, 3, 2, 1, 3, 1, 2, 4, 4, 2, 3, 1, 4, 2, 4, 3, 2, 3, 4, 3, 2, 4, 3, 2, 2, 3, 3, 3, 1, 2, 3, 1, 1, 2, 3, 3, 4, 4, 3, 1, 2, 2, 3, 3, 3, 2, 3, 2, 1, 4, 3, 1, 2, 3, 2, 2, 2, 2, 4, 2, 4, 2, 1]
plt.plot(lx, ly, color='blue')
plt.plot(lx, ly1, color='red')
plt.plot(lx, ly2, color='green')
plt.ylim(0,20)
plt.show()

print(min(ly1), max(ly1), len(ly1))
5 10 101
lxb=[]
lyb=[]
for a in set(ly1):
    lxb.append(a)
    lyb.append(ly1.count(a))

print(lxb)
print(lyb)
[5, 6, 7, 8, 9, 10]
[23, 21, 18, 15, 15, 9]
plt.hist(ly1, [4,5,6,7,8,9,10,11], rwidth=.80)
plt.xlabel("Bins- Unique X values")
plt.ylabel("Frequencies")
for i in range(len(lxb)):
    #print(lxb[i], lyb[i])
    plt.annotate(xy=[lxb[i], lyb[i]],s=lyb[i])
plt.show()

lx=[1,2,3,4,5,6]
ly=[10,12,18,5,4,6]

lx1=[1,3,5,7,9,11]
lx2=[2,4,6,8,10,12]
ly1=[10,12,18,5,4,6]
ly2=[4,6,7,15,9,12]
fs=plt.rcParams['figure.figsize']
print(fs[0])
print(fs[1])
fs[0]=6
fs[1]=4
fs=plt.rcParams['figure.figsize']
print(fs[0])
print(fs[1])
8
6
6
4
plt.bar(lx, ly, color='r', label='Total Sales')
plt.legend(loc=2)
plt.xlabel("Nos of Weeks")
plt.ylabel("Sales Amount")
plt.title("Weekly Sales Report")
plt.ylim(2,20)
for i in range(len(lx)):
     plt.annotate(xy=[lx[i],ly[i]+.5],s=ly[i])  
plt.annotate(xy=[lx[ly.index(max(ly))]+.5, max(ly)+.5],s="<-Highest Sales",
            color='green')
plt.savefig("d:/d/weeklysales.png")
plt.show()

plt.bar(lx, ly, color='blue')
plt.show()

plt.plot(lx, ly, color='red')
plt.show()

f, ((ax1, ax2), (ax3, ax4))= plt.subplots(2,2)
ax1.bar(lx, ly)
ax2.plot(lx, ly)
ax3.scatter(lx, ly)
ax4.plot(lx, ly)
plt.show()
