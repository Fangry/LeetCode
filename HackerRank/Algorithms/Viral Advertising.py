from math import floor

shared, cum_likes = 5, 0
for i in range(int(input())):
    if i != 0:
        shared = 3 * floor(shared/2)
    cum_likes += floor(shared/2)
print(cum_likes)
