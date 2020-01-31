import pyperclip
text = pyperclip.paste()
text_list = text.split('\n')
for i in range(len(text_list)):
    text_list[i] = '* '+text_list[i]
tex_out = '\n'.join(text_list)
print(tex_out)
