Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s={1,2,3,4)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
s={1,2,3,4}
s
{1, 2, 3, 4}
s=set()
s
set()
s={1,1,1,1,1,1}
s
{1}
s=
SyntaxError: invalid syntax
s={12,34,5,5,556,67,87,67}
s
{34, 67, 5, 87, 12, 556}
s=set()
s
set()
s.add(1)
s
{1}
s.add(56.899)
s
{56.899, 1}
s.add("kumar")
s
{56.899, 1, 'kumar'}
s.ad([1,2,3,4})
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
s.ad([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s.ad([1,2,3,4])
AttributeError: 'set' object has no attribute 'ad'. Did you mean: 'add'?
s.add((1,2,3))
s
{56.899, 1, 'kumar', (1, 2, 3)}
s.add({2:34,67:78})
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.add({2:34,67:78})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.dd((5,6,7))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s.dd((5,6,7))
AttributeError: 'set' object has no attribute 'dd'. Did you mean: 'add'?
s.add(8,9,6,))
SyntaxError: unmatched ')'
s.add(8,9,6,5))
SyntaxError: unmatched ')'
s.add((8,9,6,5))
s
{1, 'kumar', (1, 2, 3), (8, 9, 6, 5), 56.899}
1 in s
True
false in s
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    false in s
NameError: name 'false' is not defined. Did you mean: 'False'?
s.add(True)
s
{1, 'kumar', (1, 2, 3), (8, 9, 6, 5), 56.899}
s.add(False)
s
{False, 1, 'kumar', (1, 2, 3), (8, 9, 6, 5), 56.899}
False in s
True
False not in s
False

a={1,2,3,5,6,8,10}
b={6,7,8,9}
a | b
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.union(b)
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.intersection(b)
{8, 6}
a & b
{8, 6}
a - b
{1, 2, 3, 5, 10}
a ^ b
{1, 2, 3, 5, 7, 9, 10}
{8, 6}
{8, 6}
a <= {1}
False
a >= {1}
True
a >= {1,3,4,5,6,7,66}
False
a <= {1,3,4,5,6,7,66}
False
a >= {6,10,8}
True
a >= {1,3,4,5,6,7,66}
False
a
{1, 2, 3, 5, 6, 8, 10}
b
{8, 9, 6, 7}
a.isdisjoint(b)
False
a.isdisjoint({90,80})
True
a
{1, 2, 3, 5, 6, 8, 10}
a.add(15)
a
{1, 2, 3, 5, 6, 8, 10, 15}
a.add(78)
a
{1, 2, 3, 5, 6, 8, 10, 78, 15}
a.updated({23,22,24})
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.updated({23,22,24})
AttributeError: 'set' object has no attribute 'updated'. Did you mean: 'update'?
a.update({23,22,24})
a
{1, 2, 3, 5, 6, 8, 10, 78, 15, 22, 23, 24}
a.pop()
1
a.pop()
2
a,remove(3)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a,remove(3)
NameError: name 'remove' is not defined
a.remove(3)
a
{5, 6, 8, 10, 78, 15, 22, 23, 24}
a.remove(3)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.remove(3)
KeyError: 3
a.discard(3)
a
{5, 6, 8, 10, 78, 15, 22, 23, 24}
a.discard(10)
a
{5, 6, 8, 78, 15, 22, 23, 24}
a.discard(10)
a
{5, 6, 8, 78, 15, 22, 23, 24}
a.clear()
a
set()
a={1,4,23,57,235}
b={1,2,4,34}
a
{1, 4, 23, 57, 235}
b
{1, 2, 4, 34}
a.intersection_update(b)
a
{1, 4}
b
{1, 2, 4, 34}
c=b
c.add(12)
d
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
c
{1, 2, 34, 4, 12}
c=d
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    c=d
NameError: name 'd' is not defined. Did you mean: 'id'?
c
{1, 2, 34, 4, 12}
d=c
d.app(56)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    d.app(56)
AttributeError: 'set' object has no attribute 'app'
>>> d.add(78)
>>> d
{1, 2, 34, 4, 12, 78}
>>> d.copy(56)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    d.copy(56)
TypeError: set.copy() takes no arguments (1 given)
>>> d.copy(c)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    d.copy(c)
TypeError: set.copy() takes no arguments (1 given)
>>> d.copy(89)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    d.copy(89)
TypeError: set.copy() takes no arguments (1 given)
>>> c
{1, 2, 34, 4, 12, 78}
>>> d=c
>>> d
{1, 2, 34, 4, 12, 78}
>>> d=c.copy
>>> d.add(78)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    d.add(78)
AttributeError: 'builtin_function_or_method' object has no attribute 'add'
>>> c
{1, 2, 34, 4, 12, 78}
>>> len(c)
6
>>> min(c)
1
>>> max(c)
78
>>> sum(c)
131
>>> sorted(c)
[1, 2, 4, 12, 34, 78]
