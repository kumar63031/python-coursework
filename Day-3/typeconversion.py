Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> a
10
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> str(a)
'10'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> b=10.5
>>> b
10.5
>>> int(b)
10
>>> complex(b)
(10.5+0j)
>>> str(b)
'10.5'
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c=2+3j
c
(2+3j)
int(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(2+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
s = 'python'
j = '14567'
k = '459.789'
int(s)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
int(j)
14567
int(k)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(k)
ValueError: invalid literal for int() with base 10: '459.789'
float(s)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'python'
float(j)
14567.0
float(k)
459.789
complex(s)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
complex(j)
(14567+0j)
complex(k)
(459.789+0j)
list(s)
['p', 'y', 't', 'h', 'o', 'n']
tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
set(s)
{'p', 't', 'y', 'o', 'h', 'n'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
c=5+7j
c
(5+7j)
int(c)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
1 =[1,2,3,4]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=[1,2,3,4]
l
[1, 2, 3, 4]
int(l)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
str(l)
'[1, 2, 3, 4]'
complex(l)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
list(l)
[1, 2, 3, 4]
tuple(l)
(1, 2, 3, 4)
set(l)
{1, 2, 3, 4}
dict(l)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
