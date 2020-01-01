nt = list(map(int, input().split()))
road = list(map(int, input().split()))

for i in range(nt[1]):
    case = list(map(int, input().split()))
    print(min(road[case[0]: case[1]+1]))
