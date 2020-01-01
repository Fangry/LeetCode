for i in range(int(input())):
    g = int(input())
    rounded = (g // 5 + 1) * 5
    if rounded - g < 3 and g > 37:
        print(rounded)
    else:
        print(g)
