import re

import pyperclip

phone_number = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

email = re.compile(r'''(
[a-zA-z0-9._%+-]+
@
[a-zA-z0-9-.]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

text = str(pyperclip.paste())
match = []

for group in phone_number.findall(text):
    number = ' '.join([group[1], group[3], group[3]])
    if group[8] != '':
        number += ' x' + group[8]
    match.append(number)

for group in email.findall(text):
    match.append(group[0])

if len(match) > 0:
    pyperclip.copy(' '.join(match))
    print('Copied to clipboard')
    print('\n'.join(match))
else:
    print('No phone number or email address were found!')
