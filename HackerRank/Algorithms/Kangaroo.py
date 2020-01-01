xv = list(map(int, input().split()))
x1, v1, x2, v2 = xv[0], xv[1], xv[2], xv[3]

if x1 == x2:  # already same
    print('YES')
elif (x1 > x2 and v1 > v2) or (x1 < x2 and v1 < v2):  # slower never gonna catch up
    print('NO')
else:
    curr_dist, prev_dist = abs(x1 - x2), 10001

    # continue to jump when dist gets smaller
    while curr_dist != 0 and curr_dist < prev_dist:
        prev_dist = curr_dist
        x1 += v1
        x2 += v2
        curr_dist = abs(x1 - x2)

    if curr_dist == 0:
        print('YES')
    else:
        print('NO')
