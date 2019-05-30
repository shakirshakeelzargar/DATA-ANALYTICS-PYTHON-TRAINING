def msg():
    print("hello from msg function")
    
def msg1(name, age):
    print("Name is :", name)
    print("Age is :", age)

def msg2(name, age=0):
    print("Name is :", name)
    print("Age is :", age)

def msg4(name, age=0, subject='python'):
    print("Name is :", name)
    print("Age is :", age)
    print("subject is :", subject)

def msg3(name, subject, *mkt):
    print("Name is :", name)
    print("subject ", subject)
    print("Marks  :", mkt)
#msg()
#msg1('Rajeev',34)
#msg1(32,'ABC')
#msg1(age=32,name='ABC')
#msg2('abc',99)
#msg3('abc',9,7,7,7,7,7)
msg4('ABC','XYZ','SAS')
#msg4(name='ABC',subject='SAS')
Name is : ABC
Age is : XYZ
subject is : SAS
ls1=[3,4,5,2,4,3]
sd=getsd(ls1)
print("Value in sd ", sd)
Mean : 3.5
Standard Deviation : 0.9574271077563381
Value in sd  0.9574271077563381
import math
def getsd(ls):
    s=0
    x_mean=sum(ls)/len(ls)
    print("Mean :", x_mean)
    for l in ls:
        s=s+((l-x_mean)**2)
    print("Standard Deviation :",math.sqrt(s/len(ls)))
    return math.sqrt(s/len(ls))
x=[3,4,5,6,4]
y=[2,3,4,5,1]
CR : 0.8320502943378437
def getcr(x, y):
    A=0
    B=0
    C=0
    x_mean=sum(x)/len(x)
    y_mean=sum(y)/len(y)
    for r in range(len(x)):#0 1 2 3 4
        A=A + (x[r]-x_mean)*(y[r]-y_mean)
        B=B + (x[r]-x_mean)**2
        C=C + (y[r]-y_mean)**2
    
    print("CR :", A/math.sqrt(B*C))