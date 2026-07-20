Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = 'python programming'
len(s)
18
min(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    min(a)
NameError: name 'a' is not defined
min(s)
' '
max(s)
'y'
ord('a')
97
ord('b')
98
ord('j')
106
ord('k')
107
chr(76)
'L'
chr(107)
'k'
chr(106)
'j'
chr(1)
'\x01'
9
9
s = 'python programming'
s.uppre()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.uppre()
AttributeError: 'str' object has no attribute 'uppre'. Did you mean: 'upper'?
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'PYTHON PROGRAMMING'
"Siix8ubugn8yuigofljgyujoionCafe".casefold()
'siix8ubugn8yuigofljgyujoioncafe'
s
'python programming'
s.center(28,'-')
'-----python programming-----'
s.ljust(28,'-')
'python programming----------'
s.right(28,'-')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.right(28,'-')
AttributeError: 'str' object has no attribute 'right'
s.lright(28,'-')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s.lright(28,'-')
AttributeError: 'str' object has no attribute 'lright'
s.rjust(28,'-')
'----------python programming'
'123'.zfill(5)
'00123'
'123'.zfill(3)
'123'
'123'.zfill(2)
'123'
'123'.zfill(10)
'0000000123'
s
'python programming'
s.find('g')
10
s.fin('o')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s.fin('o')
AttributeError: 'str' object has no attribute 'fin'. Did you mean: 'find'?
s.find('o')
4
s.find('z')
-1
s.rfind('o')
9
s.index('0')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.index('0')
ValueError: substring not found
s.index('o')
4
s.rindex('o')
9
s.index('z')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s.index('z')
ValueError: substring not found
s.count('o')
2
s.count('g')
2
#replace&modify
s
'python programming'
s.replace('Python','java')
'python programming'
s.replace('python','java')
'java programming'
s.maketrans('python','123456')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.maketrans('python','123456'))
'123456 1r5grammi6g'
s = 'java,python,javascript,c,c++'
s.split(',')
['java', 'python', 'javascript', 'c', 'c++']
s.split(',',2)
['java', 'python', 'javascript,c,c++']
s.split(',',5)
['java', 'python', 'javascript', 'c', 'c++']
j = '''hxsgdyuH
HDUSGF78RUJ
DSHJGRYU'''
s.rsplit(',',3)
['java,python', 'javascript', 'c', 'c++']
>>> j = '''hxsgdyuH
... HDUSGF78RUJ
... DSHJGRYU'''
>>> j.splitlines()
['hxsgdyuH', 'HDUSGF78RUJ', 'DSHJGRYU']
>>> j.splitlines('-',1)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    j.splitlines('-',1)
TypeError: splitlines() takes at most 1 argument (2 given)
>>> j.splitlines()
['hxsgdyuH', 'HDUSGF78RUJ', 'DSHJGRYU']
>>> l = ['java', 'python', 'javascript', 'c', 'c++']
>>> ''.join(1)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    ''.join(1)
TypeError: can only join an iterable
>>> ''.join(l)
'javapythonjavascriptcc++'
>>> '_'.join(l)
'java_python_javascript_c_c++'
>>> ' '.join(l)
'java python javascript c c++'
>>> s
'java,python,javascript,c,c++'
>>> s.partition(',')
('java', ',', 'python,javascript,c,c++')
>>> s.rpartition(',')
('java,python,javascript,c', ',', 'c++')
>>> t = "Hello "
>>> t.encode()
b'Hello '
>>> b'Hello '.decode()
'Hello '
>>> t = "Hello &"
>>> t.encode()
b'Hello &'
>>> b'Hello &'.decode
<built-in method decode of bytes object at 0x000002AD7E503270>
>>> b'Hello &'.decode()
'Hello &'
