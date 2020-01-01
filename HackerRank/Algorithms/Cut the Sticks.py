n, s = int(input()), list(map(int, input().split()))


def mini(lst):
    m = 1000
    for i in lst:
        if i < m and i != 0:
            m = i
    return m

print(len(s))
while any(s):
    shortest, l, output = mini(s), len(s), 0
    for i in range(l):
        if s[i] > 0:
            s[i] -= shortest
            if s[i] > 0:
                output += 1
    if output > 0:
        print(output)
