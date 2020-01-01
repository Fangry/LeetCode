# swapping operation doesn't change # of balls in each container, the actual swapping operation is irralevent
# all impossible cases are when all containers contain unique balls except one that contains a different ball

for i in range(int(input())):
    n = int(input().strip())
    M = [list(map(int, input().split())) for i in range(n)]
    verticalSums, horiSums = [], [] # total number of a type of ball & capacity of a container

    for i in range(n):
        verticalSums.append(0)
        horiSums.append(sum(M[i]))
        for j in range(n):
            verticalSums[i] += M[j][i]

    if sorted(verticalSums) == sorted(horiSums): # sort the two lists and check if they match
        print('Possible')
    else:
        print('Impossible')
