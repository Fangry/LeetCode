# from math import ceil

n, p = int(input()), int(input())
# turns = 1

# if p == 1:
#     turns = 0
# else:
#     middle = int(n/2)
#     if p == middle:
#         turns = int(middle/2)
#     elif p < middle:
#         turns = int(p/2)
#     else:
#         if n - p == 1 and not n % 2:
#             turns = ceil((n-p)/2)
#         else:
#             turns = int((n-p)/2)

# print(turns)


# from discussion, really simple
print(min(p//2, n//2 - p//2))
