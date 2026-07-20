'''s='java programming'

if 'python' in s:
    print('python found')'''

if s[0] =='p':
    print("string is starting with p")

#if else

'''username,password= input("Enter the username and password: ").split()
if data == (username,password):
    print("login")
else:
    print("invalid login")'''

# elif ladder


'''n = int(input("Enter a number: "))

if n>0:
    print("+ve")
elif n<0:
    print("-ve")
else:
    print("Zero")'''

# nested if

products ={
    'laptops':0,
    'mouse':10,
    'charger':5,
    'phones':30,
    'kerboards':0
}


product = input("Enter the poduct: ")
if product in products:
    if products[product]!=0:
        print(f"you can buy {product}!!")
    else:
        print(f"[product] is out of stock")
else:
    print(f"{product} is not available")


