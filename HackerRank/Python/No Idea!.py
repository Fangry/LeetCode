'''
n, m = map(int, input().split())
lst = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
total = 0


# 1st attempt
# time limit exceeded
for i in range(n):
    if lst[i] in a:
        total += 1
    elif lst[i] in b:
        total -= 1
print(total)


# 2nd attempt
# list comprehension, but still time limit exceeded
print(sum([(i in a) - (i in b) for i in lst]))
'''


# 3rd attempt: 1st line of input is useless so just wrote input()
# use set on a and b, saw major time improvement
nm = input()
l = input().split()
a = set(input().split())
b = set(input().split())
total = 0


for i in l:
    if i in a:
        total += 1
    elif i in b:
        total -= 1
print(total)

