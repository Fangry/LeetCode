st = list(map(int, input().split()))
ab = list(map(int, input().split()))
mn = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
aout, oout = 0, 0

for i in range(mn[0]):
    if st[0] <= ab[0] + a[i] <= st[1]:
        aout += 1
print(aout)

for i in range(mn[1]):
    if st[0] <= ab[1] + b[i] <= st[1]:
        oout += 1
print(oout)
