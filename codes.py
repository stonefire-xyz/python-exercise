#!python3
Passwords = {'email': 'uxhce!v89[]Fv\\',
            '126': 'xslfjdslkfjsdljf'
}
import sys,pyperclip
if len(sys.argv) < 2:
    print('Uasage: you must give a class to get the passwd')
    sys.exit()
account = sys.argv[1]
if account in Passwords:
    pyperclip.copy(Passwords[account])
    print('Passwords for '+ account + ' copied to clipboard')
else:
    print('there is no account named ' + account)

