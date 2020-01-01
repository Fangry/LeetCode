for i in range(int(input())):
    b, w = list(map(int, input().split()))
    bc, wc, z = list(map(int, input().split()))
    if bc + z < wc:
        # print('case 1')
        print((bc + z)*w + bc*b)
    elif wc + z < bc:
        # print('case 2')
        print((wc + z)*b + wc*w)
    else:
        # print('case 3')
        print(b*bc + w*wc)
