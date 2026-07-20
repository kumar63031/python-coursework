'''
syntax:
    var = lambda arg : exp

#
add = lambda a,b: a+b
print(add(11,34))
print(add(71,94))
print(add(81,64))

#
wish = lambda name : f'Welcome to Python Course {name}'

print(wish('subbu'))
print(wish('kumar'))


#
gst = lambda price: (price+price*0.18)

print(gst(1000))
print(gst(6700))
print(gst(1800))

#
greatest = lambda a,b: a if a>b else b

print(greatest(100,356))
print(greatest(100,36))
print(greatest(198,56))

#
iseven = lambda a: f"{a} is even Number" if a%2 == 0 else f"{a} is Odd Number"

print(iseven(24))
print(iseven(15))
print(iseven(99))

#
bill = lambda charge: charge if charge > 99 else charge + 30

print(bill(100))
print(bill(78))
print(bill(945))

#

login = True
instock = False

status = lambda login,instock : ("You can buy product" if instock  else "product is out of stock ") if login else "Login to buy a product"

print(status(login,instock))


l = [1,2,3,4,5,6,7]
res = list(map(lambda i:i*2,l))
print(res)


names = ['subbu','nagendra','sahith']
t = list(map(lambda i:i.title(),names))
print(t)



#filter

l =[1,2,3,4,5,6,7,8,9,10,11]
res = list(filter(lambda i:i%2==0,l))
print(res)


l =[1,2,3,4,5,6,7,8,9,10,11]
res = list(filter(lambda i:i>5,l))
print(res)


l =[1,2,3,4,5,6,7,8,9,10,11]
res = list(filter(lambda i:i%3==0,l))
print(res)


from functools import reduce
l = [1,2,3,4,5,6,7,8,9,10,11,12]

s=reduce(lambda sum, i: sum+i,l)
p = reduce(lambda pro ,i:pro*i,l)
m = reduce(lambda max ,i:max if max>i else i,l)
mi = reduce (lambda max ,i: max if max<i else i,l)
print(s,p,m,mi)


'''

d ={'subbu':50,'nadendra':40,'naresh':60,'dinesh':80,'sahith':70}

print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))

print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))











