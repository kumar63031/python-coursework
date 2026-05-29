Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#python operator
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
9/2
4.5
a//b
2
9/2
4.5
a%b
0
9%2
1
2**3
8
3**2
9
a**3
8000
a
20
b
10
a<b
False
a>b
True
a<=b
False
10<=b
True
a>=b
True
a==b
False
a!=b
True
y=5
y
5
y =y+5
y
10
y +=5
y
15
y-=10
y
5
y
5
y*=5
y
25
y//=5
y
5
y%=5
y
0
y+=10
y
10
Y/=2
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    Y/=2
NameError: name 'Y' is not defined. Did you mean: 'y'?
y
10
y/=2
y
5.0
y/=2
y
2.5
y/=2
a
20
b
10
a%2==0
True
a%==0 and b%==0 and a.b
SyntaxError: invalid syntax
a%20==0 and b%20==0 and a>b
False
a%20==0 or b%20==0 or a>b
True
a%20==0 or b%20==0 or a<b
True
a%22==0 or b%20==0 or a>b
True
a%22==0 or b%20==0 or a<b
False
not a>b
False
t ={1,2,3,4,5,6}
4 in t
True
6 in t
True
65 in t
False
50 not in t
True
d ={'egg':10, 'oil':50, 'sugar':34}
d in 'sugar'
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    d in 'sugar'
TypeError: 'in <string>' requires string as left operand, not dict
'sugar' in d
True
a = 'python programming'
a
'python programming'
'y' in a
True
'g' in a
True
's' in a
False
l =['java', 'python', 'mysql', 'c++']
'java, in l
SyntaxError: unterminated string literal (detected at line 1)
'java' in l
True
'c++' inl
SyntaxError: invalid syntax
'c++' in l
True
'html' in l
False
t = ('laptop', 'keyboard', 'mouse', 'mobile',)
'laptop' in t
True
'ball' in t
False
t = {1,2,3,4,5,6,57,89}
t
{89, 1, 2, 3, 4, 5, 6, 57}
5 in t
True
8 not in t
True
899 not in t
True
57 in t
True
d = {'egg':10, 'oil':25, 'sugar':35, 'salt':45}
120 in d
False
'egg' in d
True
'sugar' not in d
False
'cap' in d
False
l = [1,2,3,4,5]
m = [1,2,3,4,5]
>>> l==m
True
>>> n=m
>>> n
[1, 2, 3, 4, 5]
>>> l is m
False
>>> n is m
True
>>> id(l)
2292012944448
>>> id(m)
2292013116416
>>> id(n)
2292013116416
>>> l is not m
True
>>> n is not l
True
>>> #bitwise operators
>>> 8 & 15
8
>>> 8 7 7
SyntaxError: invalid syntax
>>> 8 & 7
0
>>> 8 | 7
15
>>> 9 | 7
15
>>> 10^11
1
>>> 13^6
11
>>> 8>>2
2
>>> 15>>1
7
>>> 16<<2
64
>>> 4<<2
16
#input and output
print(f'a={a} b={b} c={c}')
print("a=",a, 'b=',b 'c=',sep='',end='@@@@')
print('a= %d b=%.2f c=%s'%(a,b,c))
print('a= {} b={} c= {]'.fotamt(a,b,c))
