# time limit exceeded
'''
nd = list(map(int, input().split()))
lst = list(map(int, input().split()))

newLst = [None] * nd[0]
for i in range(nd[0]):
    counter = nd[1]
    temp = i
    while counter > 0:
        temp -= 1
        counter -= 1
        if temp == -1:
            temp = nd[0] - 1
    newLst[temp] = lst[i]

for x in newLst:
    print(x, end=' ')
'''

# d left rotations = n - d right rotations

nd = list(map(int, input().split()))
lst = list(map(int, input().split()))
newLst = [None] * nd[0]

for i in range(nd[0]):
    newLst[(i - nd[1]) % nd[0]] = lst[i]

for x in newLst:
    print(x, end= ' ')


