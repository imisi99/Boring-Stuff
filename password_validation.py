import re


def password_validator(password):
    if not re.search(r'[!@#$%^&*():<>.,/`"\\{}]', password):
        print('Password must contain at least one special character!')
    if not re.search(r'[A-Z]', password):
        print('Password must mave at least one Upper case character!')
    if not re.search(r'[a-z]', password):
        print('Password must mave at least one lower case character!')
    if not re.search(r'[0-9]', password):
        print('Password must contain at least on digit')
    if len(password) < 8:
        print('Password must be 8 characters long')
    else:
        print('Nice password')


x = input('Enter password: ')
password_validator(x)
