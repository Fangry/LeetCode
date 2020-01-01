d1, d2 = list(map(int, input().split())), list(map(int, input().split()))
if d1[2] < d2[2]:
    print(0)
elif d1[2] > d2[2]:
    print(10000)
else:
    if d1[1] < d2[1]:
        print(0)
    elif d1[1] > d2[1]:
        print((d1[1] - d2[1])*500)
    else:
        if d1[0] > d2[0]:
            print((d1[0] - d2[0])*15)
        else:
            print(0)
