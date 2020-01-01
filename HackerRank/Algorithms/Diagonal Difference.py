n = int(input())
m = []
for i in range(n):
    m += list(map(int, input().split()))


def diagonalDifference(lst):
    left_sum, right_sum = 0, 0
    for i in range(n):
        left_sum += lst[i*n+i]
        right_sum += lst[(i+1)*n-i-1]
        # print(lst[i*n+i], lst[(i+1)*n-i]-1)
    return abs(left_sum - right_sum)


print(diagonalDifference(m))
