for i in range(int(input())):
    n, m, s = list(map(int, input().split()))
    if (m+s-1) % n == 0:
        print(n)
    else:
        print((m+s-1) % n)
