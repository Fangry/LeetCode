# problem statement is wrong

n, k = list(map(int, input().split()))
clouds = list(map(int, input().split()))
i = k % n
e = 100 - clouds[i] * 2 - 1

while i != 0:
    i = (i + k) % n
    e -= clouds[i] * 2 + 1

print(e)
