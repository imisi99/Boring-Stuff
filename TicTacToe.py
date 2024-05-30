import time

my_board = {'top-L': '', 'top-M': '', 'top-R': '',
            'mid-L': '', 'mid-M': '', 'mid-R': '',
            'low-L': '', 'low-M': '', 'low-R': ''}


def draw_board(board):
    print(f'{board['top-L']} | {board['top-M']} | {board['top-R']}')
    print('--+---+--')
    print(f'{board['mid-L']} | {board['mid-M']} | {board['mid-R']}')
    print('--+---+--')
    print(f'{board['low-L']} | {board['low-M']} | {board['low-R']}')


turn = 'X'
i = 9
while 0 <= i <= 9:
    if i == 0:
        draw_board(my_board)
        break
    print(i)
    time.sleep(1)
    draw_board(my_board)
    print('Available slots: ')
    for x, j in my_board.items():
        if j == '':
            print(f'{x}', end=', ')
            time.sleep(0.1)
    print()
    move = input(f'Enter a slot to play {turn}: ')
    if move not in my_board.keys():
        time.sleep(0.5)
        print('Invalid slot')
        time.sleep(0.5)
        continue
    else:
        i -= 1
        if my_board[move] == '':
            my_board[move] = turn
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        else:
            time.sleep(0.5)
            print('Slot already taken, select one from available slots')
            time.sleep(0.5)
            continue

