# My first list
shoplist = ['apple','banana','apple','melon']
print('The shoplist is :',end = ' ')
for item in shoplist:
    print(item,end = ' ')
print('')
shoplist.append('pear')
print('The shoplist is :',end = ' ')
for item in shoplist:
    print(item,end = ' ')
print('')
del shoplist[0]

for item in shoplist:
    print(item,end = '\ ' )
