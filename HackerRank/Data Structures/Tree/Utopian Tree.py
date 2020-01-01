for i in range(int(input())):
    height = 1
    for j in range(int(input())):
        if j % 2 == 0:
            height *= 2
        else:
            height += 1
    print(height)
