Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# input declaration
name = input()
subbu
name
'subbu'
name = input("Enter your name: ")
Enter your name: kumar
name
'kumar'
age = input("Enter your age: ")
Enter your age: 22
age
'22'
age = int(input("Enter your age: "))
Enter your age: 22
age
22
type(age)
<class 'int'>
gpa = float(input("Enter your cpa: "))
Enter your cpa: 7.8
gpa
7.8
type(gpa)
<class 'float'>
'subbu narendra kumar sai eswar'
'subbu narendra kumar sai eswar'
'subbu narendra kumar sai eswar'.spilt()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    'subbu narendra kumar sai eswar'.spilt()
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
'subbu narendra kumar sai eswar'.spilt(" ")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    'subbu narendra kumar sai eswar'.spilt(" ")
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
'subbu narendra kumar sai eswar'.spilt(' ')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    'subbu narendra kumar sai eswar'.spilt(' ')
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
names = input("enter the names: ").split
enter the names: subbu kumar sai eswar 
names
<built-in method split of str object at 0x0000026494D4A7F0>
names = input("enter the names: ").split()
enter the names: subbu kumar sai eswar
names
['subbu', 'kumar', 'sai', 'eswar']
products = input("enter the product names: ").split()
enter the product names: laptop mouse keyborad charger
products
['laptop', 'mouse', 'keyborad', 'charger']
topics = tuple(input("enter the topics: ").split())
enter the topics: tokens operators variables comments
topics
('tokens', 'operators', 'variables', 'comments')
op = set(input("enter the operators names: ").split())
enter the operators names: in not in is is not and 
op
{'not', 'is', 'in', 'and'}
list(map(int,input("enter your marks: ").split()))
enter your marks: 89 65 78 56
[89, 65, 78, 56]
prices =tuple(map(int,input("enter your prices: ").split()))
enter your prices: 768 567 43 78 90
prices
(768, 567, 43, 78, 90)
rating =set(map(int,input("enter your ratings: ").split()))
enter your ratings: 4 5 2 5 4 3 3 4
rating
{2, 3, 4, 5}
per = list(map(int,input("enter the values of pers: ").split))
enter the values of pers: 
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    per = list(map(int,input("enter the values of pers: ").split))
TypeError: 'builtin_function_or_method' object is not iterable
per = list(map(float,input("enter the values of pers: ").split))
enter the values of pers: 7.6 89.9 98.0 84.8
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    per = list(map(float,input("enter the values of pers: ").split))
TypeError: 'builtin_function_or_method' object is not iterable
per = list(map(float,input("enter the values of pers: ").split()))
enter the values of pers: 7.6 89.9 98.0 84.8
per
[7.6, 89.9, 98.0, 84.8]
prices = tuple(map(float,input("enter the prices : ").split()))
enter the prices : 78 67 56 97
prices
(78.0, 67.0, 56.0, 97.0)
prices = set(map(float,input("enter the prices : ").split()))
enter the prices : 89 67 89 68 78
prices
{89.0, 67.0, 68.0, 78.0}
a,b = 10,20
a
10
b
20
a,b = [10,20]
a
10
b
20
a,b,c,d = list(map(int,input("enter the 4 sides: ").split))
enter the 4 sides: 33 5 6 7
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a,b,c,d = list(map(int,input("enter the 4 sides: ").split))
TypeError: 'builtin_function_or_method' object is not iterable
a,b,c,d = list(map(int,input("enter the 4 sides: ").split()))
enter the 4 sides: 4 5 8 9
a
4
b
5
c
8
d
9
username,password = list(map(input()).split())
codegnan c@567
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    username,password = list(map(input()).split())
TypeError: map() must have at least two arguments.
username,password = list(map(input("enter username& password;").split()))
enter username& password;kumar c@3567
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    username,password = list(map(input("enter username& password;").split()))
TypeError: map() must have at least two arguments.
price,discount = list(map(float,input("enter price and discount: ").split))
enter price and discount: 56789 98
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    price,discount = list(map(float,input("enter price and discount: ").split))
TypeError: 'builtin_function_or_method' object is not iterable
price,discount = list(map(float,input("enter price and discount: ").split()))
enter price and discount: 78 89
price
78.0
discount
89.0
a= eval(input())
897.88
a
897.88
>>> a= eval(input())
98067
>>> a
98067
>>> type(a)
<class 'int'>
>>> a= eval(input())
[1,22,4,6,7]
>>> a
[1, 22, 4, 6, 7]
>>> a= eval(input())
(2,4,5,7,8)
>>> a
(2, 4, 5, 7, 8)
>>> a= eval(input())
{1,3,4,3,4,6,7}
>>> a
{1, 3, 4, 6, 7}
>>> a= eval(input())
{3: 7, 4: 8, 5: 9}
>>> a
{3: 7, 4: 8, 5: 9}
>>> a= eval(input())
True
>>> a
True
>>> type(a)
<class 'bool'>
>>> a
True
>>> a= 'codegnan'
>>> b= 'pfs'
>>> a+b
'codegnanpfs'
>>> a
'codegnan'
>>> a*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
>>> ('codegnan ')*10
'codegnan codegnan codegnan codegnan codegnan codegnan codegnan codegnan codegnan codegnan '
>>> 'pyrhon '*5
'pyrhon pyrhon pyrhon pyrhon pyrhon '
