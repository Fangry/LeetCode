n = int(input())
a = list(map(int, input().split()))
output = 1000
for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            output = min(output, abs(i - j))
if output == 1000:
    print(-1)
else:
    print(output)
