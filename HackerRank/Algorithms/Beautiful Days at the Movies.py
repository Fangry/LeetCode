i, j, k = list(map(int, input().split()))
output = 0

for i in range(i, j+1):
    if (i - int(str(i)[::-1])) % k == 0:
        output += 1

print(output)
