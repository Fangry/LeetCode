n = int(input())
path = input()
elevation = 0
num_valleys = 0

for i in range(n):
    if path[i] == 'D':
        elevation -= 1
    else:
        elevation += 1
        if elevation == 0:
            num_valleys += 1

print(num_valleys)
