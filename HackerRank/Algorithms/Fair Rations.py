# n = int(input())
# b = list(map(int, input().split()))
# s = sum(b)

# if s % 2 != 0:
#     print('NO')
# else:
#     output = 0
#     for i in range(n):
#         if b[i] % 2 != 0:
#             b[i] += 1
#             b[i + 1] += 1
#             output += 2
#             print(b)
#     print(output)

# a more optimal solution
n, b, s, output = int(input()), list(map(int, input().split())), 0, 0
for x in b:
    s += x
    if s % 2:
        output += 2
print(output if s % 2 == 0 else 'NO')
