from math import sqrt, floor, ceil

text = input().replace(' ', '')
leng = len(text)
sqrtLen = sqrt(leng)
c, r = ceil(sqrtLen), floor(sqrtLen)
if c * r < leng:
    r += 1

matrix, row, counter, rowCounter = [], [], 0, 0
while counter < leng:
    row.append(text[counter])
    rowCounter += 1
    counter += 1
    if rowCounter == c:
        rowCounter = 0
        matrix.append(row)
        row = []
if rowCounter > 0:
    for i in range(r * c - leng):
        row.append('`')
    matrix.append(row)

for i in range(c):
    for j in range(r):
        if matrix[j][i] != '`':
            print(matrix[j][i], end='')
    print(end=' ')