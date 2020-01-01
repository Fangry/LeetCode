s, n, output = input(), int(input()), 0
for c in s:
    if c == 'a':
        output += 1
output *= n // len(s)
for c in s[:n % len(s)]:
    if c == 'a':
        output += 1
print(output)
