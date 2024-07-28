import math
def printTable(data, rowLen):
    # get longest number
    sortedData = list(data)
    sortedData.sort()
    cellSize = len(str(sortedData[-1]))
    if len(data) <= rowLen:
        printASingleRow(data, cellSize, True, rowLen)
    else:
        for i in range(math.ceil(len(data)/rowLen)):
            printASingleRow(data[i*rowLen:(i+1)*rowLen], cellSize, i == 0, rowLen)


def printASingleRow(rowData, cellSize, isFirstRow, rowLen):
    # fill short row
    if len(rowData) < rowLen:
        for i in range(rowLen - len(rowData)):
            rowData.append(' ')
    # print upper border
    if isFirstRow:
        temp = []
        for i in range(len(rowData)):
            prepareCellBorder(temp, cellSize, i+1 == rowLen)
        print(*temp, sep='')
    # print content
    temp = []
    for i, item in enumerate(rowData):
        prepareCellContent(temp, str(item), cellSize, i+1 == rowLen)
    print(*temp, sep='')

    # print lower border
    temp = []
    for i in range(len(rowData)):
        prepareCellBorder(temp, cellSize, i+1 == rowLen)
    print(*temp, sep='')

def prepareCellBorder(temp, size, closed):
    temp.append('+')
    for i in range(size):
        temp.append('-')
    if closed:
        temp.append('+')

def prepareCellContent(temp, number, size, closed):
    temp.append('|')
    for i in range(size - len(number)):
        temp.append(' ')
    temp.append(number)
    if closed:
        temp.append('|')

input = [4,12,93,8938,87324,8,9809,345325,98234234,0,234234234]
printTable(input, 5)