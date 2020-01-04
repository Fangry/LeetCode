nq = list(map(int, input().split()))
abk = [list(map(int, input().split())) for i in range(nq[1])]
arr = [0 for i in range(nq[0]+1)]


# time litmit exceeded
'''
for i in range(nq[1]):
    for j in range(nq[0]):
        if abk[i][0] <= j+1 <= abk[i][1]:
            arr[j] += abk[i][2]

print(max(arr))
'''


for i in range(nq[1]):
    a, b, k = abk[i][0], abk[i][1], abk[i][2]

    arr[a-1] += k
    arr[b] -= k

    print(arr)

m = x = 0
for a in arr:
    x += a
    if m < x:
        m = x

print(m)
