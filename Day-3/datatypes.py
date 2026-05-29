Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> a
10
>>> type(a)
<class 'int'>
>>> b=9.67
>>> b
9.67
>>> type(b)
<class 'float'>
>>> c=2+8j
>>> c
(2+8j)
>>> type(c)
<class 'complex'>
>>> s='kumar'
>>> s
'kumar'
>>> type(s)
<class 'str'>
>>> l=[1,3,4,6]
>>> l
[1, 3, 4, 6]
>>> type(l)
<class 'list'>
>>> t=(1,3,4,6,8)
>>> t
(1, 3, 4, 6, 8)
>>> type(t)
<class 'tuple'>
>>> set{1,4,5,6,6,7}
SyntaxError: invalid syntax
>>> s={2,4,,4,6,,7,7}
SyntaxError: invalid syntax
>>> s={2,3,2,5,7,8}
>>> s
{2, 3, 5, 7, 8}
>>> type(s)
<class 'set'>
>>> d={'kumar'='kum', 'course'= 'python'}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
d={"kumar"="kum", "age"=10}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
d={'kumar':'kum', 'age':10}
d
{'kumar': 'kum', 'age': 10}
type(d)
<class 'dict'>
status=true
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    status=true
NameError: name 'true' is not defined. Did you mean: 'True'?
status='true'
status='false'
status(2)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    status(2)
TypeError: 'str' object is not callable
status
'false'
print(status)
false
type(status)
<class 'str'>
