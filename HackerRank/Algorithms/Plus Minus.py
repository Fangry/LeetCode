n = int(input())
ar = list(map(int, input().split()))
output = [0, 0, 0]

for i in range(n):
    if ar[i] > 0:
        output[0] += 1
    elif ar[i] < 0:
        output[1] += 1
    else:
        output[2] += 1

for i in range(3):
    print(round(output[i]/n, 6))
