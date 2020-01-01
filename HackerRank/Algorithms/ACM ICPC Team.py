# too slow
# n, m = list(map(int, input().split()))
# know = [input() for i in range(n)]
# maxTopics, maxWays = 0, 0

# for i in range(n - 1):
#     for j in range(i + 1, n):
#         tmpTopics = 0
#         for k in range(m):
#             if know[i][k] == '1' or know[j][k] == '1':
#                 tmpTopics += 1
#         if tmpTopics > maxTopics:
#             maxTopics = tmpTopics
#             maxWays = 1
#         elif tmpTopics == maxTopics:
#             maxWays += 1

# print(maxTopics)
# print(maxWays)


# faster
n, m = list(map(int, input().split()))
know = [int(input(), 2) for i in range(n)]
maxTopics, maxWays = 0, 0

for i in range(n - 1):
    for j in range(i + 1, n):
        tmpTopics = bin(know[i] | know[j]).count('1')
        if tmpTopics > maxTopics:
            maxTopics = tmpTopics
            maxWays = 1
        elif tmpTopics == maxTopics:
            maxWays += 1

print(maxTopics)
print(maxWays)
