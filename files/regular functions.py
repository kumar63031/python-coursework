
'''
import re

pattern = '[abc]'
text = 'codegnan'

res = re.match(pattern,text)

print(res.group() if res else "No Match FOund")



# search
import re

pattern = '[A-Z]'
text = 'Codegnan3.11'

res = re.search(pattern,text)

print(res.group() if res else "No Match FOund")


#find all elemnts
import re

pattern = '[0-9]'
text = 'Codegnan 3.11'

res = re.findall(pattern,text)

print(res)



#find with index
import re

pattern = '[n]'
text = 'Codegnan3.11'

res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())



# exact same
import re

pattern ='[1-9]{9}'
text = '987654321'

res = re.fullmatch(pattern,text)

print(res.group() if res else "No Match FOund")


#splitting
import re

pattern = r'[,a+yn]'
text = 'java,python,c++'

res = re.split(pattern,text)

print(res)


'''


#replace

import re

pattern = r'[[0-9]{2}'
text = 'python: 34 mysql : 78 java : 55 html : 45'






























