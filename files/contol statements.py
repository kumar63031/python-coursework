# str list tuple set dict range()

'''
for var in seq:
    print(var)


s = 'python programming'
for i in s:
    print(i)


l = ['sugar', 'salt', 'oil', 'eggs']
for i in l:
    print(i)


t = ('1.intro','2.tokens','3.Data types')
for i in t:
    print(i)


s = {'laptop','Mouse','keyboard'}
for i in s:
    print(i)


d = {'name':'kumar','batch':55,'course':'PFS','skills':['python','mysql','java']}
for i in d:
    print(i,d[i])


'''

# range(start,stop+1,step) => (0,n,1)

'''

for i in range(1,11):
    print(i)

for i in range(2,51,2):
    print(i)

for i in range(5,101,5):
    print(i)

for i in range(20,0,-1):
    print(i)

for i in range(30,2,-3):
    print(i)

#length

s = 'looping statements'

for i in range(len(s)):
    print(i,s[i])

l = [7,2,4,8,3,1,5]
for i in range(len(l)):
    print(i,l[i])

l = (7,2,4,8,3,1,5)
for i in range(len(l)):
    print(i,l[i])

# enumerate

s ='looping'
for i in enumerate(s):
    print(i[0],i[1])

l = [7,2,4,8,3,1,5]
for i in enumerate(l):
    print(i[0],i[1])


t = (7,2,4,8,3,1,5)
for i in enumerate(t):
    print(i[0],i[1])


k = [7,2,4,8,3,1,5]
for i in enumerate(k):
    print(i[0],i[1])

'''
'''
# break , continue, pass
for i in range(10):
    pass

for i in range(10):
    if i==5:
        break
    print(i)


for i in range(10):
    if i==5:
        continue
    print(i)

'''
'''
s = 'looping statements'
for i in s:
    if i in 'aeiouAEIOU':
        print(i)


l = [56,76,32,3,34,3,2,5,97,45,13,23,45]
for i in l:
    if i%2==0:
        print(i)


d = {'laptops':0,'chargers':2,'keyboard':10,'phones':15,'tab':0,'mouse':5}
for i in d:
    if d[i]:
        print(i)


t = (9,2,13,4,5,6)
for i in range(len(t)):
    print(i*t[i])
'''

names = {'subbu','naresh','dinesh','sahith','rushi','praneeth'}
for i in names:
    if(names.upper()):
        print(i)
         

