#Seperating Lists
def seperate(my_list):
    new_value = ''
    for i in range(len(my_list) - 1):
        new_value += f'{my_list[i]}' + ', '
        if i == (len(my_list) - 2):
            new_value = new_value + f'and {my_list[-1]}'
    new_value.replace(" ", ",")
    print(new_value, sep= ',')


tryout = ['david', 'daniel', 'samuel', 'skinny', 'miracle']
seperate(tryout)



#Picture grid
grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
    ]

for j in range (6):
    if j != 0:
        print()
    for i in range(len(grid)):
        print(grid[i][j], end= '')

