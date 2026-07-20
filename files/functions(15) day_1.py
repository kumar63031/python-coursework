'''
def function_name(arg):
    #statements
    return

function_name(para)


def wish(name):
    print(f'Welcome to the python course {name}!')


wish('subbu')
wish('praneeth')
wish('rishita')
wish('sai durga')


def iseven(num):
    if num%2==0:
        return f"{num} - Even number"
    else :
        return f"{num} - Odd number"
print(iseven(12))
print(iseven(13))



def factorial(num):
    fact=1
    for i in range(1,num+1):
        if fact*=i:
            return fact

num = int(input())
print("factorial:",factorial(num))




def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num} - Not Prime Number"
    return f"{num} - Prime Number"

num = int(input())
print(isprime(num))



# positional arguments

def display(name, email, pwd):
    print("Name: ",name)
    print("Email: ",email)
    print("Password: ",pwd)
display('subbu','subbu@gmail.com','subbu@123')
display('subbu@gmail.com','subbu','subbu@123')
display('subbu@gmail.com','subbu@123','subbu')


#key (we must give key values to the diplay function)




# default argument


def display(name, email, pwd=''):
    print("Name: ",name)
    print("Email: ",email)
    print("Password: ",pwd)
display('subbu','subbu@gmail.com','subbu@123')
display('subbu@gmail.com','subbu')



 # variable arguments

def display(*names):
    print("names:",names)

display('subbu','dinesh','naresh','akhil','nagendra')
display('naresh','akhil','nagendra') 
display('subbu','dinesh','naresh','akhil')
display('nagendra')
display('subbu','dinesh')

'''

# variable key arguments

def display(**names):
    print("names:",names)

display(k1='subbu',k2='naresh',k3='nagendra')
display(k1='nagendra') 
display(k1='subbu',k2='dinesh')


















