a="12.80"
print(type(a))
b=float(a)
print(type(b))
<class 'str'>
<class 'float'>
ls=[10,11,12,13,14,15,16]
type(ls)
list
#ls[0] # 10
#ls[0:3] # 10,11,12
#ls[0:5:2] #10,12,14
#ls[-1] #16
#ls[6:1:-1] # 16, 15, 14, 13, 12, 11, 10
#ls*2 #repeat the complete list
#----
#len(ls) 
#max(ls)
#min(ls)
sum(ls)
91
print(ls)
#ls.insert(2,88) #insert(<index>, <values>)
#ls.append(99) #append(<value>)
#del ls[2] # ls[<index>]
#r=ls.pop(2) #ls.pop(<index>)
ls.remove(14) #ls.remove(<value>)
print(ls)
#print("deleted values is ", r)
[16, 15, 14, 13, 12, 12, 11, 11, 10]
[16, 15, 13, 12, 12, 11, 11, 10]
ls=[10,11,12,13,14,15,16]
ls=ls+[11,12] #concatination
ls
[10, 11, 12, 13, 14, 15, 16, 11, 12]
#ls.count(11) #count of given value in the list
#ls.index(12) #return the first index of given value in list
#ls.sort(reverse=False) #sort the list ascending
#ls.sort(reverse=True) #sort the list in descending
print(ls)
[16, 15, 13, 12, 12, 11, 11, 10]
ls[2]=22
ls
[16, 15, 22, 12, 12, 11, 11, 10]
ls=(10,11,12,13,14,15,16)
type(ls)
tuple
ls[0] # 10
ls[0:3] # 10,11,12
ls[0:5:2] #10,12,14
ls[-1] #16
ls[6:1:-1] # 16, 15, 14, 13, 12, 11, 10
ls*2 #repeat the complete list
(10, 11, 12, 13, 14, 15, 16, 10, 11, 12, 13, 14, 15, 16)
ls.append(99) #Error as it Tuple
ls.insert(2,99) #Error as it Tuple
ls.remove(14) #Eroor as it Tuple
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-58-60d9ba366578> in <module>()
----> 1 ls.append(2,99)
      2 ls.remove(14)

AttributeError: 'tuple' object has no attribute 'append'
ls + (33,44) #concatenation in tuple
ls*2 #repeating the tuple values
(10, 11, 12, 13, 14, 15, 16, 10, 11, 12, 13, 14, 15, 16)
ls[0]=33 #Error 'tuple' object does not support item assignment
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-63-386df5363973> in <module>()
----> 1 ls[0]=33

TypeError: 'tuple' object does not support item assignment
sr="IndianCricketTeam" #as good as tuple 
sr[0:5:2]
sr[0]="T" #Error 'str' object does not support item assignment
sr.append('T')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-69-815d13f85fb3> in <module>()
      1 sr="IndianCricketTeam"
      2 sr[0:5:2]
----> 3 sr[0]="T" #Error 'str' object does not support item assignment
      4 sr.append('T')

TypeError: 'str' object does not support item assignment
d={'name':'rajeev','location':'Noida',99:90}
#type(d)
d['name']='Satish' #override the existing values of given key
d
d['Course']='Python' #add new key values pair in dictionary
d
{99: 90, 'Course': 'Python', 'location': 'Noida', 'name': 'Satish'}
d.keys()
d.values()
d.items()
dict_items([('name', 'Satish'), ('location', 'Noida'), (99, 90), ('Course', 'Python')])
del d['name']
d
{99: 90, 'Course': 'Python', 'location': 'Noida'}
ls=[3,4,5,6]
print(type(ls))
tp=tuple(ls)
print(type(tp))
<class 'list'>
<class 'tuple'>
ls=['name','course','fees']
d={}
d=d.fromkeys(ls)
d
{'course': None, 'fees': None, 'name': None}
print("Hello"); print("Hi")
Hello
Hi
#operators:
#airthmetic
a=10
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
12
8
20
5.0
0
100
#relation/comparision operator 
#>,<,>=,<=,!=,==, in 
print(a)
print(b)
#print(a>b)
#print(a>=b)
#print(a>5 and b>5) #True <and> False => T-T => T, F-T=>F , T-F=>F, F-F=F
#print(a>5 or b>5) #True <or> False => T-T => T, F-T=>T , T-F=>T, F-F=F
#print(11 in [12,10,13]) #check the list validation
#print(11 not in [12,10,13]) 
10
2
True
#conditions
#if..else..
#-1 - if
a=1
if(a>5):
    print("a is > 5")
print("Hello")
Hello
#-2 - if --else
a=1
if(a>5):
    print("a is > 5")
else:
    print("a is not >5")
print("Hello")
a is not >5
Hello
#-2 - if --else nested
a=10
b=3
if(a>5):
    if(b>5):
        print("a is > 5 and b is >5")
    else:
        print("a is >5 but is not >5")
else:
    print("a is not >5")
print("Hello")
a is >5 but is not >5
Hello
#-2 - if --elseif ...else
a=10
if(a>10):
    print("a is > 10")
elif( a> 5):
    print("a is > 5")
else:
    print("a is not >5")
print("Hello")
a is > 5
Hello
ls=[11,22,33,44]
num=11
if(num in ls):
    print(num ,"num is in list")
else:
    print(num, " num is not in list")
11 num is in list
num=int(input(" Enter a number "))
print(type(num))
print("Value entered by user is ", num)

if num % 2==0:
    print("Given num is even")
else:
    print("Given num is odd")
 Enter a number 23
<class 'int'>
Value entered by user is  23
Given num is odd
msg=input("Enter a values with comma sep.")
print("entered msg is ", msg)
ls= msg.split(",")
print("Data in list ", ls)
Enter a values with comma sep.22,33,44
entered msg is  22,33,44
Data in list  ['22', '33', '44']
ls[0]=int(ls[0])
ls[1]=int(ls[1])
ls[2]=int(ls[2])
print(ls)
max(ls)
[22, 33, 44]
44
#WAP to accept three numbers and showing highest one
num1=int(input(" Num - 1 "))
num2=int(input(" Num - 2 "))
num3=int(input(" Num - 3 "))

if (num1> num2 and num1>num3):
    print("Highest is ", num1)
elif (num2> num1 and num2>num3):
    print("Highest is ", num2)
elif (num3> num1 and num3>num2):
    print("Highest is ", num3)
else:
    print("Number are equal")
 Num - 1 11
 Num - 2 11
 Num - 3 11
Number are equal
lmarks=[44,55,99,88]
lname=['A','B','C','D']
lname[lmarks.index(max(lmarks))]
'C'
#loops
#while
a=1
while(a<10):
    a=a+1
    if(a==4):
        continue #skip the rest of loop execution
    if(a==8):
        break #close the loop
    print(a)    
2
3
5
6
7
num1=3
a=1
while(a<=10):
    print(a, "*", num1, "=",a*num1)
    a=a+1
1 * 3 = 3
2 * 3 = 6
3 * 3 = 9
4 * 3 = 12
5 * 3 = 15
6 * 3 = 18
7 * 3 = 21
8 * 3 = 24
9 * 3 = 27
10 * 3 = 30
*
**
***
****
*****
***
**
*
a=1
while(a<=5):
    print("*"*a)
    a=a+1
a=a-1
while(a>=1):
    print("*"*a)
    a=a-1
*
**
***
****
*****
*****
****
***
**
*
#for
for a in [11,22,33,44]:
    print(a)
11
22
33
44
list(range(10))
list(range(2,10))
list(range(2,10,2))
[2, 4, 6, 8]
for a in range(1,10,2):
    print(a)
1
3
5
7
9
ls=[('Rajeev',55,88),('Raj',50,80)]
for a in ls:
    for b in a:
        print(b)
    print(a)
Rajeev
55
88
('Rajeev', 55, 88)
Raj
50
80
('Raj', 50, 80)
lsales=[100,120,125,130,135,140]
lproduct=['A','B','A','C','A','B']
d={}
for a in range(6):
    if lproduct[a] not in d.keys():
        print("Creating a dictionary key ", lproduct[a])
        d[lproduct[a]]=lsales[a]
        print("Current Values of d ", d)
    else:
        print("updating a dictionary key ", lproduct[a])
        d[lproduct[a]]=d[lproduct[a]]+lsales[a]
        print("Current Values of d ", d)
d
    
Creating a dictionry key  A
Current Values of d  {'A': 100}
Creating a dictionry key  B
Current Values of d  {'A': 100, 'B': 120}
updating a dictionry key  A
Current Values of d  {'A': 225, 'B': 120}
Creating a dictionry key  C
Current Values of d  {'A': 225, 'B': 120, 'C': 130}
updating a dictionry key  A
Current Values of d  {'A': 360, 'B': 120, 'C': 130}
updating a dictionry key  B
Current Values of d  {'A': 360, 'B': 260, 'C': 130}
{'A': 360, 'B': 260, 'C': 130}
d={}
d=d.fromkeys(lproduct)
print(d)
for a in d.keys():
    d[a]=0
print(d)

for a in range(6):
    print("Updating for ", lproduct[a], "with value ", lsales[a])
    d[lproduct[a]] =d[lproduct[a]]+lsales[a]
    print(d)
    
print(d)
{'A': None, 'B': None, 'C': None}
{'A': 0, 'B': 0, 'C': 0}
Updating for  A with value  100
{'A': 100, 'B': 0, 'C': 0}
Updating for  B with value  120
{'A': 100, 'B': 120, 'C': 0}
Updating for  A with value  125
{'A': 225, 'B': 120, 'C': 0}
Updating for  C with value  130
{'A': 225, 'B': 120, 'C': 130}
Updating for  A with value  135
{'A': 360, 'B': 120, 'C': 130}
Updating for  B with value  140
{'A': 360, 'B': 260, 'C': 130}
{'A': 360, 'B': 260, 'C': 130}
ls=[]
for a in range(5):
    ls.append(int(input("Enter a number - ")))
Enter a number - 10
Enter a number - 20
Enter a number - 30
Enter a number - 40
Enter a number - 50
ls
[10, 20, 30, 40, 50]
ls=[10,10,20,30,40,20,10]
for l in set(ls):
    print(l)
40
10
20
30