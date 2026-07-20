Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={'komalatha':45,'bhargavi':67,'subbu':78,'nagendra':89,'dinesh':50}
d.keys()
dict_keys(['komalatha', 'bhargavi', 'subbu', 'nagendra', 'dinesh'])
d.items()
dict_items([('komalatha', 45), ('bhargavi', 67), ('subbu', 78), ('nagendra', 89), ('dinesh', 50)])
sorted(d)
['bhargavi', 'dinesh', 'komalatha', 'nagendra', 'subbu']
max(d)
'subbu'
min(d)
'bhargavi'
len(d)
5
d
{'komalatha': 45, 'bhargavi': 67, 'subbu': 78, 'nagendra': 89, 'dinesh': 50}
d['dinesh']
50
d['dinesh']=100
d
{'komalatha': 45, 'bhargavi': 67, 'subbu': 78, 'nagendra': 89, 'dinesh': 100}
d['komalatha']=60
d
{'komalatha': 60, 'bhargavi': 67, 'subbu': 78, 'nagendra': 89, 'dinesh': 100}
d['rishi']=87
d
{'komalatha': 60, 'bhargavi': 67, 'subbu': 78, 'nagendra': 89, 'dinesh': 100, 'rishi': 87}
>>> d.update({'praneeth':90,'manideep':80})
>>> d
{'komalatha': 60, 'bhargavi': 67, 'subbu': 78, 'nagendra': 89, 'dinesh': 100, 'rishi': 87, 'praneeth': 90, 'manideep': 80}
>>> d.popitem()
('manideep', 80)
>>> d
{'komalatha': 60, 'bhargavi': 67, 'subbu': 78, 'nagendra': 89, 'dinesh': 100, 'rishi': 87, 'praneeth': 90}
>>> d.popitem()
('praneeth', 90)
>>> d.popitem['dinesh']
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d.popitem['dinesh']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> d
{'komalatha': 60, 'bhargavi': 67, 'subbu': 78, 'nagendra': 89, 'dinesh': 100, 'rishi': 87}
>>> d.popitem()
('rishi', 87)
>>> d.pop('subbu')
78
>>> d
{'komalatha': 60, 'bhargavi': 67, 'nagendra': 89, 'dinesh': 100}
>>> del d['komalatha']
>>> d
{'bhargavi': 67, 'nagendra': 89, 'dinesh': 100}
>>> d.clear()
>>> d
{}
>>> d={'komalatha': 60, 'bhargavi': 67, 'subbu': 78, 'nagendra': 89, 'dinesh': 100, 'rishi': 87, 'praneeth': 90, 'manideep': 80}
>>> d
{'komalatha': 60, 'bhargavi': 67, 'subbu': 78, 'nagendra': 89, 'dinesh': 100, 'rishi': 87, 'praneeth': 90, 'manideep': 80}
>>> d.setdefault('rishi'0)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> d.setdefault('rishi',0)
87
>>> d.default('kumar',0)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d.default('kumar',0)
AttributeError: 'dict' object has no attribute 'default'. Did you mean: 'setdefault'?
>>> d.setdefault('kumar',0)
0
