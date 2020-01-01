# slower solution, doesn't pass case 14 & 15, but u don't need to sort stations
# n, m = list(map(int, input().split()))
# stations = list(map(int, input().split()))
# lst = []
# output = 0
# for i in range(n):
#     dist = 100000
#     for j in range(m):
#         temp = abs(i - stations[j])
#         if temp == 0:
#             dist = 0
#             break
#         elif temp < dist:
#             dist = temp
#     lst.append(dist)
# print(max(lst))

# faster solution, returns the max. distance of leftmost, middle, and rightmost stations
n, m = list(map(int, input().split()))
stations = sorted(list(map(int, input().split())))
lst = [stations[0], n - stations[-1] - 1]
cities = []
counter = 0

for i in range(n):
    if i in stations:
        cities.append(1)
    else:
        cities.append(0)

for i in range(n):
    if cities[i] == 1:
        lst.append(int((counter + 1) / 2))
        counter = 0
    else:
        counter += 1

print(max(lst))

