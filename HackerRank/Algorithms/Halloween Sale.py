pdms = list(map(int, input().split()))
p, d, m, s = int(pdms[0]), int(pdms[1]), int(pdms[2]), int(pdms[3])
output = 0

while s >= p:
    s -= p
    output += 1
    if p - d < m:
        p = m
    else:
        p -= d

print(output)

