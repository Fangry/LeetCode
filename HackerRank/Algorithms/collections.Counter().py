from collections import Counter

x, n, c = int(input()), Counter(list(map(int, input().split()))), int(input())
revenue = 0

for i in range(c):
    size, price = map(int, input().split())
    if n[size]:
        income += price
        n[size] -= 1

print(revenue)
