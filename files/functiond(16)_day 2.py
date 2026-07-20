
'''
#local scope


def display():
    n = 10
    print("Inside: ",n)
display()
print("Outside: ",n)


#global scope

def display():
    global n
    n =10
    print("Inside:",n)

display()
print("Outside:",n)


def display():
    global n
    n+=10
    print("Inside:",n)

n = 10
display()
print("Outside:",n)


#Non local

def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner function:",n)
    inner()

    print("Outer function:",n)
outer()


#int float complex str list tuple set dict boo


def update(n):
    n+=10
    print("Inside:",n)

n = 10
update(n)
print("Outside:",n)


def update(n):
    n+=10
    print("Inside:",n)

n = 10.4
update(n)
print("Outside:",n)


def update(n):
    n+=10
    print("Inside:",n)

n =5+7j
update(n)
print("Outside:",n)




def update(n):
    n=n+"prog"
    print("Inside:",n)

n = 'python'
update(n)
print("Outside:",n)


def update(n):
    n.append(8)
    print("Inside:",n)

n = [1,2,3,4]
update(n)
print("Outside:",n)



def update(n):
    n=n+(8,)
    print("Inside:",n)

n = (1,2,3,4)
update(n)
print("Outside:",n)


def func(num):
    if num == 0:
        return
    print(num,end=' ')
    func(num-1)
    print(num,end=' ')

func(5)



def sumofdigits(n):
    if n ==0:
        return 0
    return n+sumofdigits(n-1)
print(sumofdigits(5))


def power(base,pow):
    if pow==0:
        return 1
    return base*power(base,pow-1)
print(power(2,4))
print(power(3,3))

'''

def reverseofstr(s,ind):
    if ind == 0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)

l = "Python Programming"
print(reverseofstr(l,len(l)-1))













































