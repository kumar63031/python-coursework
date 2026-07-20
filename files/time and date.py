
'''
from datetime import date,time,datetime,timedelta
t = date.today()
print(t)
print("Year:", t.year)
print("Month:",t.month)
print("Day:",t.day)
print("Weekday from 0:",t.weekday())
print("Weekday from 1:",t.isoweekday())


from datetime import date,time,datetime,timedelta
t = date(2026,1,30)

print(t)


from datetime import date,time,datetime,timedelta
t = time(23,8,36)
print(t)


from datetime import date,time,datetime,timedelta
n = datetime.now()

print(n)
print("Year:", n.year)
print("Month:",n.month)
print("Day:",n.day)
print("Hour:",n.hour)
print("Minute:",n.minute)
print("second:",n.second)


from datetime import date,time,datetime,timedelta

n = datetime.now()

print(n.strftime('%d/%m/%y'))
print(n.strftime('%d/%m/%y %H:%M:%S'))
print(n.strftime('%d/%m/%y %I:%M:%S %p'))
print(n.strftime('%d %b %y %I:%M:%S %p'))
print(n.strftime('%d %B %y %I:%M:%S %p'))
print(n.strftime('%a %d %B %y %I:%M:%S %p'))
print(n.strftime('%A %d %B %y %I:%M:%S %p'))



from datetime import date,time,datetime,timedelta
n = datetime.now()

n15 = n+timedelta(minutes=15)
n2 = n+timedelta(hours=2)
n7 = n+timedelta(days=60)

print(n15,n2,n7,sep='\n')


try :
    a= int(input("Enter the age: "))
    print(12/0)
    print(b)
    print(13+'14')
    d = {1:1,2:2,3:3,4:4}
    print(d[5])
    l=[1,2,3]
    print(l[10])
except ValueError:
    print("Enter the age in a digit[0-9] format")
except ZeroDivisionError:
    print("can't divide with zero")
except NameError:
    print("define the var")
except TypeError:
    print("Add the sane datatypes")
except KerError:
    print("Key is not present")
except IndexError:
    print("Index is out of range")
else:
    print("Age:",a)
finally:
    print("Thankyou")
          

try :
    a= int(input("Enter the age: "))
    print(12/0)
    print(b)
    print(13+'14')
    d = {1:1,2:2,3:3,4:4}
    print(d[5])
    l=[1,2,3]
    print(l[10])

except Exception as e:
    print("Error Occured:",e)
else:
    print("No Error Occured:")
finally:
    print("Thankyou")

'''

try:
    amount = int(input("Enter amount to withdraw: "))
    if amount < 0:
        raise Exception("Enter the amount greater than zero")
    
except Exception as e:
    print("Error Occured:",e)
else:
    print("No Error Occured:")
finally:
    print("Thankyou")



































