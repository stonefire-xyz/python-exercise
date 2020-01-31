import pyperclip
vimfile = open('/home/killer/.config/nvim/init.vim')
pyperclip.copy(vimfile.read())
vimfile.close()
