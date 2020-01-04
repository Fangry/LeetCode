n = int(input())
strings = [input() for i in range(n)]
q = int(input())
queries = [input() for i in range(q)]

for i in range(q):
    count = 0
    for j in range(n):
        if queries[i] == strings[j]:
            count += 1
    print(count)
