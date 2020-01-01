nk = list(map(int, input().split()))
ar = list(map(int, input().split()))
count = 0

for i in range(nk[0]):
    for j in range(i+1, nk[0]):
        if (ar[i] + ar[j]) % nk[1] == 0:
            count += 1
            # print(ar[i], ar[j])

print(count)