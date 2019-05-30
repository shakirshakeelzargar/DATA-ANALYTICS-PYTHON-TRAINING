try:
    a=10
    b=0
    c=a/b    
    print("Result is ",c)
except ZeroDivisionError:
    print("Trying to divide by zero")
except TypeError:
    print("Invalid numeric values")
except NameError:
    print("Variable not found")
except: 
    print("Variable not found")
else:
    print("NO error code executed successfully...")
finally:
    print("Transaction executed.")
#ZeroDivisionError 
#TypeError
#NameError  
Trying to divide by zero
Transaction executed.
Result is=>  5.0
a=10
b=0
c=a/b    
print("Result is ",c)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-13-83d30d6ce1f5> in <module>()
      1 a=10
      2 b=0
----> 3 c=a/b
      4 print("Result is ",c)

ZeroDivisionError: division by zero