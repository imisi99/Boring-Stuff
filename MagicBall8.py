import random
import time

message = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outllook no so good',
    'Very doubtful'
]

while True:
    question = input('What question do you have for the wise one? ').lower().strip()
    if question == "":
        response = 'Bruh be serious!'
    elif question == 'nothing':
        response = 'Then what are you doing here?'
    else:
        response = message[random.randint(0, len(message) - 1)]
    time.sleep(1)
    print(response)
    time.sleep(2)
    print('Do you have any other question(Y/N)')
    reply = input().lower()
    if reply == 'y':
        continue
    elif reply == 'n':
        break
    else:
        print('Program exited due to invalid keyword')
        time.sleep(1)
        break