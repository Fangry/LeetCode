# slower
# for i in range(int(input())):
#     nk, arrivals = list(map(int, input().split())), list(
#         map(int, input().split()))
#     on_time = 0
#     for j in range(nk[0]):
#         if arrivals[j] <= 0:
#             on_time += 1
#     if on_time >= nk[1]:
#         print('NO')
#     else:
#         print('YES')

# faster by using sort
for i in range(int(input())):
    nk, arrivals = list(map(int, input().split())), sorted(list(
    map(int, input().split())))
    print('YES' if sum( 1 for a in arrivals if a <= 0) < nk[1] else 'NO')
    


