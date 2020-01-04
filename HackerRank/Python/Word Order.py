n = int(input())
words = [input() for i in range(n)]

count = {}
for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1

print(len(count))
for v in count.values():
    print(v, end=' ')