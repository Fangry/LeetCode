nk = list(map(int, input().split()))
heights = list(map(int, input().split()))

doses = max(heights) - nk[1]
if doses > 0:
    print(doses)
else:
    print(0)
