'''
pin = 1234
for i in range(5):
    e_pin = int(input("Enter the pin: "))
    if e_pin == pin:
        print("Unlock the phone: ")
        break
    else:
        print("Incorrect pin")
else:
    print("Try again, after 60 seconds")
    
l =[2,3,5,6,8,10,34,12]
num = int(input())
for i in range(len(l)):
    if l[i]== num:
        print(f'{num} is found at index -{i}')
        break
else :
    print(f'{num} is not found')

  


password = input("Enter the password: ")
if len(password) >= 8:
    s=set()
    for i in password:
        if i.isupper():
            s.add('u')
        elif i.islower():
            s.add('l')
        elif i.isdigit():
            s.add('d')
        else:
            s.add('s')

    if len(s)==4:
        print("Strong password")
    else:
        print("Weak password")
else:
    print("Weak password")


'''


        
    
    

        
