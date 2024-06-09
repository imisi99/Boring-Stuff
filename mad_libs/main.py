import re

text = open('text.txt', 'r')
text_content = text.read()

mad_libs = re.compile(r'ADJECTIVE|NOUN|VERB')
change = mad_libs.findall(text_content)
for i in change:
    if i == 'ADJECTIVE':
        enter = input('Enter an adjective: ')
        text_content = text_content.replace('ADJECTIVE', f'{enter}', 1)
    if i == 'VERB':
        enter = input('Enter a verb: ')
        text_content = text_content.replace(f'VERB', f'{enter}', 1)
    if i == 'NOUN':
        enter = input('Enter a noun: ')
        text_content = text_content.replace(f'NOUN', f'{enter}', 1)

print(text_content)
