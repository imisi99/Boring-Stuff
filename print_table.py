tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]


def print_table(table):
    max_length0 = 0
    max_length1 = 0
    max_length2 = 0
    for index, i in enumerate(table):
        if index == 0:
            for data in i:
                length = len(data)
                if length > max_length0:
                    max_length0 = length
        if index == 1:
            for data in i:
                length = len(data)
                if length > max_length1:
                    max_length1 = length
        if index == 2:
            for data in i:
                length = len(data)
                if length > max_length2:
                    max_length2 = length
    print(max_length2)
    print(max_length1)
    print(max_length0)


print_table(tableData)
