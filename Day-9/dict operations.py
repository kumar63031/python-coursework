Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
d=dict()
d={'k1':'val', 'k2':'val'}
d
{'k1': 'val', 'k2': 'val'}
d={]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
d={}
d{1}='int'
SyntaxError: invalid syntax
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['demo']='str'
d
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d[False]='bool'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex', False: 'bool'}
SyntaxError: invalid syntax
SyntaxError: invalid syntax
d={}
d[1]=1
d
{1: 1}
d[23]=23.4
d[3]='ghygh'
d[4]=3+6j
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]={1,3}
d[8]={1:1,2:4}
d[9]=False
d
{1: 1, 23: 23.4, 3: 'ghygh', 4: (3+6j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 1, 2: 4}, 9: False}
d[1]=14
d
{1: 14, 23: 23.4, 3: 'ghygh', 4: (3+6j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 1, 2: 4}, 9: False}
d={}
d[1]=14
d
{1: 14}
d={}
d[1]=2
d[2]=2
d[3]=3
d[4]=2
d
{1: 2, 2: 2, 3: 3, 4: 2}
d[3]
3
>>> d={1:2,2:4,3:6,4:8,5:10,6:12}
>>> d[4]
8
>>> d[6]
12
>>> d={]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> d={'komalatha':45,'bhargavi':67,'subbu':78,'nagendra':89}
>>> d
{'komalatha': 45, 'bhargavi': 67, 'subbu': 78, 'nagendra': 89}
>>> d['bhargavi']
67
>>> d['subbu']
78
>>> d['komalatha']
45
>>> d['sahith']
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    d['sahith']
KeyError: 'sahith'
>>> d.get('sahith')
>>> d.get('dinesh')
>>> d.get('subbu')
78
>>> d.get(,akhil','user not found')
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> d.get('akhil','user not found')
...       
'user not found'
>>> d.get('subbu','user not found')
...       
78
>>> d
...       
{'komalatha': 45, 'bhargavi': 67, 'subbu': 78, 'nagendra': 89}
>>> d={'komalatha':45,'bhargavi':67,'subbu':78,'nagendra':89}
...       
>>> d={}
...       
