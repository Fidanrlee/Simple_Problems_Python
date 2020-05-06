
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    colWidths = [0] * len(table)
    for x in range(len(table)):
        for y in table[x]:
            if colWidths[x] < len(y):
                colWidths[x] = len(y)

    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(colWidths[y]), end = ' ')
        print()

printTable(tableData)