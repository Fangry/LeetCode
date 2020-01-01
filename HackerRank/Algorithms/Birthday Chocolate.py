s = int(input())
choco = list(map(int, input().split()))
dm = list(map(int, input().split()))
output = 0

for i in range(s):
    bar, val = 0, 0
    for j in range(i, s):
        if bar > dm[1] or val + choco[j] > dm[0]:
            break
        bar += 1
        val += choco[j]
        # print(bar, val)
        if bar == dm[1] and val == dm[0]:
            output += 1

print(output)
