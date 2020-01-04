# method 1: using deques
'''
from collections import deque

for i in range(int(input())):
    n = int(input())
    cubes = deque(map(int, input().split()))
    bottom = float('inf')

    while len(cubes) > 0:
        if cubes[0] <= bottom and cubes[-1] <= bottom:
            if cubes[0] < cubes[-1]:
                bottom = cubes[-1]
                cubes.pop()
            else:
                bottom = cubes[0]
                cubes.popleft()
        elif cubes[0] <= bottom:
            bottom = cubes[0]
            cubes.popleft()
        elif cubes[-1] <= bottom:
            bottom = cubes[-1]
            cubes.pop()
        else:
            break

    if len(cubes):
        print('No')
    else:
        print('Yes')
'''


# method 2: no deque used
# basically checks if cubes list has largest numbers on the two ends and smallest numbers in the middle
# if we can fully get to index i-1, this means the cube list is indeed structured like a "mountain" so print yes
for i in range(int(input())):
    n = int(input())
    cubes = list(map(int, input().split()))

    i = 0
    while i < n - 1 and cubes[i] >= cubes[i+1]:
        i += 1
    while i < n - 1 and cubes[i] <= cubes[i+1]:
        i += 1

    print('Yes' if i == n - 1 else 'No')
