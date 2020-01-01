from math import sqrt

for i in range(int(input())):
    a, b = list(map(int, input().split()))
    print(int(sqrt(b))-int(sqrt(a - 1)))
