t = int(input())
for i in range(t):
    ncm = list(map(int, input().split()))
    n, c, m, wrap, choco = ncm[0], ncm[1], ncm[2], 0, 0

    # spend all money frist
    temp1 = divmod(n, c)
    wrap += temp1[0]
    choco += temp1[0]
    n = temp1[1]

    # exchange wraps
    while wrap // m > 0:
        temp2 = divmod(wrap, m)
        choco += temp2[0]
        wrap = temp2[0] + temp2[1]

    print(choco)
