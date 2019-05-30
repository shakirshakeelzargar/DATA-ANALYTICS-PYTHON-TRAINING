import pymysql as ms
A=ms.connect("148.72.232.172","Test","Test#4321","Test_Antrix")
B=A.cursor()
NR=B.execute("select * from Sample where dept='HRA'")
#cl=B.description
#print(cl)
#print("column names are:")
#for c in cl:
#    print(c[0])
print("Nos of rows available ", NR)
rs=B.fetchall() #for all records
#rs=B.fetchone() #for one records
#rs=B.fetchmany(3)#for specific records
#print(rs[2])
for r in rs:
    print(r)
Nos of rows available  2
(9, 'Sandeep', 8900.0, datetime.date(2013, 4, 2), 'HRA')
(10, 'Ranjeet', 8900.0, datetime.date(2013, 4, 2), 'HRA')
#print(cl)
c_name=[]
for c in cl:
    c_name.append(c[0])

print(c_name)
print("--------")
print(rs)
['id', 'name', 'salary', 'start_Date', 'dept']
--------
((3, 'Rajat', 611.0, datetime.date(2014, 11, 15), 'IT'), (4, 'Rayan', 100.0, datetime.date(2014, 10, 15), 'HR'), (78, 'Rohit', 10000.0, datetime.date(2017, 11, 15), 'ADMIN'), (9, 'Sandeep', 8900.0, datetime.date(2013, 4, 2), 'HRA'), (10, 'Ranjeet', 8900.0, datetime.date(2013, 4, 2), 'HRA'))
c_name=[]
for c in cl:
    c_name.append(c[0])
    
for r in rs:
    for i in range(len(c_name)):
        print(c_name[i],":", r[i])
    print("--------")
id : 3
name : Rajat
salary : 611.0
start_Date : 2014-11-15
dept : IT
--------
id : 4
name : Rayan
salary : 100.0
start_Date : 2014-10-15
dept : HR
--------
id : 78
name : Rohit
salary : 10000.0
start_Date : 2017-11-15
dept : ADMIN
--------
id : 9
name : Sandeep
salary : 8900.0
start_Date : 2013-04-02
dept : HRA
--------
id : 10
name : Ranjeet
salary : 8900.0
start_Date : 2013-04-02
dept : HRA
--------
id- 3
name - rajat
salary- 611
start_date- 15-11-2014
dept-IT
db=ms.connect("148.72.232.172","Test","Test#4321","Test_Antrix")
cr=db.cursor()
NR=cr.execute("select * from Sample")
print("Nos of rows available ", NR)
rs=cr.fetchall() #for all records
for r in rs:
    print(r)
Nos of rows available  5
(3, 'Rajat', 611.0, datetime.date(2014, 11, 15), 'IT')
(4, 'Rayan', 100.0, datetime.date(2014, 10, 15), 'HR')
(78, 'Rohit', 10000.0, datetime.date(2017, 11, 15), 'ADMIN')
(9, 'Sandeep', 8900.0, datetime.date(2013, 4, 2), 'HRA')
(10, 'Ranjeet', 8900.0, datetime.date(2013, 4, 2), 'HRA')
db=ms.connect("148.72.232.172","Test","Test#4321","Test_Antrix")
cr=db.cursor()
NR=cr.execute("insert into Sample \
              values(11,'Rohit',900,'2013-04-02','HRA')")
print("Nos of Rows Affected ", NR)
db.commit()
db.close()
Nos of Rows Affected  1
db=ms.connect("148.72.232.172","Test","Test#4321","Test_Antrix")
cr=db.cursor()
NR=cr.execute("Update Sample set salary=1900 where id=11")
print("Nos of Rows Affected ", NR)
db.commit()
db.close()
Nos of Rows Affected  3
db=ms.connect("148.72.232.172","Test","Test#4321","Test_Antrix")
cr=db.cursor()
NR=cr.execute("Delete from Sample where id=11")
print("Nos of Rows Affected ", NR)
db.commit()
db.close()
Nos of Rows Affected  3
db=ms.connect("148.72.232.172","Test","Test#4321","Test_Antrix")
cr=db.cursor()
NR=cr.execute("select school,sex, count(*) from Student_Batch \
              group by school, sex")
print("Nos of rows available ", NR)
rs=cr.fetchall() #for all records
for r in rs:
    print(r)
Nos of rows available  4
('GP', 'F', 183)
('GP', 'M', 166)
('MS', 'F', 25)
('MS', 'M', 21)
db=ms.connect("148.72.232.172","Test","Test#4321","Test_Antrix")
cr=db.cursor()
NR=cr.execute("select * from Student_Batch")
print("Nos of rows available ", NR)
rs=cr.fetchall() #for all records
#for r in rs:
#    print(r)
Nos of rows available  395
rs
(('GP', 'F', 183), ('GP', 'M', 166), ('MS', 'F', 25), ('MS', 'M', 21))
d1={}
d_school={}
d_gender={}

for r in rs:
    if r[0]+":"+r[1] not in d1.keys():
        d1[r[0]+":"+r[1]]=1
    else:
        d1[r[0]+":"+r[1]]=d1[r[0]+":"+r[1]]+1
    
    if r[0] not in d_school.keys():
        d_school[r[0]]= 1
    else:
        d_school[r[0]]= d_school[r[0]]+ 1
    
    if r[1] not in d_gender.keys():
        d_gender[r[1]]=1
    else:
        d_gender[r[1]]= d_gender[r[1]]+1
        
print(d1)
print(d_gender)
print(d_school)
{'GP:F': 183, 'GP:M': 166, 'MS:M': 21, 'MS:F': 25}
{'F': 208, 'M': 187}
{'GP': 349, 'MS': 46}
d1={}
d_school={}
d_gender={}

for r in rs:
    if r[0]+":"+r[1] not in d1.keys():
        d1[r[0]+":"+r[1]]=r[2]
    else:
        d1[r[0]+":"+r[1]]=d1[r[0]+":"+r[1]]+r[2]
    
    if r[0] not in d_school.keys():
        d_school[r[0]]= r[2]
    else:
        d_school[r[0]]= d_school[r[0]]+ r[2]
    
    if r[1] not in d_gender.keys():
        d_gender[r[1]]=r[2]
    else:
        d_gender[r[1]]= d_gender[r[1]]+r[2]
        
print(d1)
print(d_gender)
print(d_school)
{'GP:F': 183, 'GP:M': 166, 'MS:F': 25, 'MS:M': 21}
{'F': 208, 'M': 187}
{'GP': 349, 'MS': 46}
d_total={}
d_count={}
for r in rs:
    if r[3] not in d_total.keys():
        d_total[r[3]] =r[7]
    else:
        d_total[r[3]] =d_total[r[3]]+ r[7]
    
    if r[3] not in d_count.keys():
        d_count[r[3]]=1
    else:
        d_count[r[3]]=d_count[r[3]]+1
print(d_total)
print(d_count)

for d in d_total.keys():
    #print("Value at ",d , "is ", d_total[d])
    #print("Value at Count ",d , "is ", d_count[d])
    d_total[d]=d_total[d]/d_count[d]

print(d_total)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-63-f2f9e017d146> in <module>()
      2 d_count={}
      3 for r in rs:
----> 4     if r[3] not in d_total.keys():
      5         d_total[r[3]] =r[7]
      6     else:

IndexError: tuple index out of range
db=ms.connect("148.72.232.172","Test","Test#4321","Test_Antrix")
cr=db.cursor()
NR=cr.execute("select mJob, avg(G1) from Student_Batch\
              group by mjob")
print("Nos of rows available ", NR)
rs=cr.fetchall() #for all records
for r in rs:
    print(r)
Nos of rows available  5
('at_home', Decimal('10.4576'))
('health', Decimal('12.2059'))
('other', Decimal('10.1773'))
('services', Decimal('11.3883'))
('teacher', Decimal('11.5345'))
import pyodbc 
db = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=.;"
                      "Database=HRM;"
                      "Trusted_Connection=yes;")

cr = db.cursor()
rs=cr.execute('SELECT * FROM Candidate')

for row in rs:
    print(row)   
(1, 'Rajiv', Decimal('12000.0000'), 1200, 'HR')
(2, 'Sandeep', Decimal('9000.0000'), 900, 'HR')
(3, 'Satish', Decimal('7000.0000'), 700, 'FN')
(3, 'Satish', Decimal('7000.0000'), 700, 'FN')
(4, 'Mohit', Decimal('15000.0000'), 1500, 'FN')