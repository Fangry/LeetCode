n = int(input())
clouds = list(map(int, input().split()))

if n < 3:
    print(1)
else:
    i = 0
    total = 0

    while i < n-3:
        if clouds[i+2] == 0:
            i += 2
        else:
            i += 1
        total += 1

    print(total+1)
   
    