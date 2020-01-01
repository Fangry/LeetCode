# not optimized, timeout for case 6-9

num_players = int(input())
scores = list(map(int, input().split()))
num_alice = int(input())
alice = list(map(int, input().split()))

# for i in range(num_alice):
#     rank = 1
#     if num_players > 1:
#         for j in range(num_players-1):
#             if alice[i] >= scores[j]:
#                 print(rank)
#                 break
#             elif scores[j+1] != scores[j]:
#                 rank += 1

#         if alice[i] < scores[-1]:
#             print(rank+1)
#         elif alice[i] < scores[-2]:
#             print(rank)
#     else:
#         if alice[i] >= scores[0]:
#             print(1)
#         else:
#             print(2)


# an optimized solution from the discussion

unique_scores = list(reversed(sorted(set(scores))))
cases_left = num_alice - 1
rank = 0
ans = []

while cases_left >= 0:
    if rank >= len(unique_scores) or unique_scores[rank] <= alice[cases_left]:
        ans.append(rank+1)
        cases_left -= 1
    else:
        rank += 1

for x in reversed(ans):
    print(x)
