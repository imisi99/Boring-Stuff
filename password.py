# This is an insecure password locker program designed to help get their saved password21ddd
import pyperclip
import sys

Passwords = {'email': '',
             'github': ''}

if len(sys.argv) < 2:
    print('Usage: python password.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in Passwords:
    if Passwords[account] != '':
        pyperclip.copy(Passwords[account])
        print(f'Password for {account} copied to clipboard')
    else:
        print('There is no password associated with this account')
        create = input('Enter a password for this account')
        Passwords[account] = create
        print('Password stored successfully')
        pyperclip.copy(Passwords[account])
else:
    print(f'There is no account {account}')
    create = input('Would you like to create a password for the account(Y/N)').lower()
    if create == 'y':
        Passwords[account] = ''
    else:
        sys.exit()
