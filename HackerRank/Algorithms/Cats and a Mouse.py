for i in range(int(input())):
    pos = list(map(int, input().split()))
    catA, catB = abs(pos[0] - pos[2]), abs(pos[1]-pos[2])
    if catA == catB:
        print('Mouse C')
    elif catA < catB:
        print('Cat A')
    else:
        print('Cat B')
