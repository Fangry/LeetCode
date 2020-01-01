n = int(input())
mapp = [[d for d in input()] for i in range(n)]


for i in range(1, n - 1):
    for j in range(1, n - 1):
        if mapp[i][j] > max(mapp[i + 1][j], mapp[i - 1][j], mapp[i][j + 1], mapp[i][j -1]):
            mapp[i][j] = 'X'

for r in mapp:
    print(''.join(r))