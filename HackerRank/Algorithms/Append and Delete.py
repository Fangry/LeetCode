s, t, k = input(), input(), int(input())
match = 0

for i in range(min(len(s), len(t))):
    if s[i] == t[i]:
        match += 1
    else:
        break

# step-by-step check, there are total of 4 cases to check
if k < len(s) + len(t) - 2*match:
    print('No')
elif k % 2 == (len(s) + len(t) - 2*match) % 2:
    print('Yes')
elif k > len(s) + len(t):
    print('Yes')
else:
    print('No')
