import pyperclip
import re
mm=pyperclip.paste()
print(mm+'\n')
wordRegex=re.compile(r'Plug .*')
jj=wordRegex.findall(mm)
for i in jj:
    print(i)

