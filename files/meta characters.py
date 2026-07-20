
'''
import re

pattern = r'h.t\b'
text = 'hot hit het hrt hat hood heart hjt h$t'

res = re.findall(pattern,text)
print(res)


#starting with

import re

pattern = r'^h'
text = 'hot hit het hrt hat hood heart hjt h$t'

res= re.findall(pattern,text)
print(res)



#ends with

import re

pattern = r't$'
text = 'hot hit het hrt hat hood heart hjt h$t'

res= re.findall(pattern,text)
print(res)



import re

pattern = r'to?'
text = 'too to t tooooooo toooooooooo'

res= re.findall(pattern,text)
print(res)


# [] this is used to check letters

import re

pattern = r'[a-z]{4,5}'
text = 'sejbjn ajdnje efji ijfi jerubv'

res = re.findall(pattern,text)
print(res)



# () this is used to match excat string

import re

pattern = r'(python)'
text = 'pyth pthon python pyhgg'

res = re.findall(pattern,text)
print(res)



#valid name 
import re

pattern = r'^[a-zA-Z]{2,15}( [a-zA-Z]{2,15})+$'
name = input("Enter the text: ")
res= re.fullmatch(pattern,name)
print("Valid format" if res else "Invalid format")



#valid email

import re

pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-z]{2,}$'
mail = input("Enter the mail: ")
res = re.fullmatch(pattern,mail)
print("Valid format" if res else "Invalid format")


#validating number

import re

pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
number = input("Enter the text: ")
res = re.fullmatch(pattern,number)
print("Valid format" if res else "Invalid format")




#validating Password

import re

pattern = r'^(?=.*[A-z])(?=.[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}'
number = input("Enter the text: ")
res = re.fullmatch(pattern,number)
print("Valid format" if res else "Invalid format")

'''

import re

pattern = r'^[a-zA-Z0-9]{5,15}$'
number = input("Enter the text: ")
res = re.fullmatch(pattern,number)
print("Valid format" if res else "Invalid format")

























