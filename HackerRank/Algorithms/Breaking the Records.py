n = int(input())
scores = list(map(int, input().split()))
bmax, bmin = scores[0], scores[0]
cmax, cmin = 0, 0

for i in range(1, n):
    if scores[i] > bmax:
        cmax += 1
        bmax = scores[i]
    elif scores[i] < bmin:
        cmin += 1
        bmin = scores[i]

print(cmax, cmin)
