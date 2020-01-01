nk = list(map(int, input().split()))
chap = list(map(int, input().split()))
page, special = 1, 0

for i in range(nk[0]):
    prob = 0
    while prob < chap[i]:
        for j in range(nk[1]):
            if prob >= chap[i]:
                break
            prob += 1
            if page == prob:
                special += 1
                # print(page)
        page += 1

print(special)
