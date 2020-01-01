bnm = list(map(int, input().split()))
k, m = sorted(list(map(int, input().split()))), sorted(
    list(map(int, input().split())))

if bnm[0] < k[0] + m[0]:
    print(-1)
elif bnm[0] == k[0] + m[0]:
    print(k[0] + m[0])
else:
    highest = 0
    for i in range(bnm[1]):
        if k[i] >= bnm[0]:
            break
        for j in range(bnm[2]):
            total = k[i] + m[j]
            if total > bnm[0]:
                break
            if total > highest:
                highest = total

    print(highest)
