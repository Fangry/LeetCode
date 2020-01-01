nm = list(map(int, input().split()))
a, b = list(map(int, input().split())), list(map(int, input().split()))
output = 0

for i in range(1, 1000):
    test1, test2 = True, True

    for j in range(nm[0]):
        if i % a[j] != 0:
            test1 = False
            break

    if test1:
        for j in range(nm[1]):
            if b[j] % i != 0:
                test2 = False
                break

    if test1 and test2:
        output += 1
        # print(ab[i])

print(output)
