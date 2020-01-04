from collections import deque

n = int(input())
ops = [input().split() for i in range(n)]
d = deque()

for op in ops:
    if op[0] == 'append':
        d.append(op[1])
    elif op[0] == 'pop':
        d.pop()
    elif op[0] == 'popleft':
        d.popleft()
    elif op[0] == 'appendleft':
        d.appendleft(op[1])

for x in d:
    print(x, end=' ')
