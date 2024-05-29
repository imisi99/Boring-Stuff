# Naming cats
x = int(input('how many cats do you have? '))
CatLists = []

for i in range (x):
    name = input(f'What is the name of cat{len(CatLists) + 1} ')
    CatLists.append(name)

print('The cat names are:')
for i in CatLists:
    print(' '+ i)


def seperate(my_list):
    new_value = ''
    for i in range(len(my_list) - 1):
        new_value = new_value + ' ' + f'{my_list[i]}'
        if i == (len(my_list) - 2):
            new_value = new_value + f' and {my_list[-1]}'
    new_value.strip("")
    print(new_value)


tryout = ['david', 'daniel', 'samuel', 'skinny', 'miracle']
seperate(tryout)

