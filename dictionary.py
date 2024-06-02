import pprint
birthday = {'Imisioluwa': 'Jan 32', 'Precious': 'May 30', 'Emmanuel': 'Feb 25'}

while True:
    name = input('Whose birthday date do we need(enter blank to exit): ')

    if name == '':
        break
    elif name in birthday.keys():
        print(f'{birthday[name]} is the birthday of {name}')
    else:
        print(f'There is no information on {name}')
        response = input('Would you like for the information to be stored in the database?(Y/N): ').lower()
        if response == 'y':
            date = input(f'Enter the birthday date for {name}: ')
            birthday[name] = date
            print('Data has been stored successfully')
            print(f'{birthday[name]} is the birthday of {name}')
        else:
            continue


message = ('There was once a time where i was lost and without hope, But i am glad that i pushed through and made it '
           'today and that time is every single fucking day!')
count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] += 1

print(pprint.pformat(count))
