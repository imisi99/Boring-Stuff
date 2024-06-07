tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]


def print_table(table):
    max_length = [0, 0, 0]
    for index, i in enumerate(table):
        for data in i:
            length = len(data)
            if length > max_length[index]:
                max_length[index] = length
    for row in zip(*table):
        print(' '.join([data.rjust(max_length[index]) for index, data in enumerate(row)]))


print_table(tableData)
