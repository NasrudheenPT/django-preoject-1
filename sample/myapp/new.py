import re
email ='adarsh@gmail.com'
a = re.findall(r'^\w+([\.\_]?\w+]*@\w+([\.]+\w+)+$',email)
print(a)