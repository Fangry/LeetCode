n = int(input())
socks = list(map(int, input().split()))
pairs = 0
to_be_paired = []

for i in range(n):
    if socks[i] not in to_be_paired:
        to_be_paired.append(socks[i])
    else:
        to_be_paired.remove(socks[i])
        pairs += 1

print(pairs)
