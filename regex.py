import re
phoneNumRegx = re.compile(r'\d{4}-\d{7}')
mo = phoneNumRegx.search('My num is 0370-7039335')
print(mo.group()
)

