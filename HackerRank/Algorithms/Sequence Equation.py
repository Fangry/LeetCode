n, nums = int(input()), list(map(int, input().split()))
for i in range(1, n + 1):
    print(nums.index(nums.index(i) + 1) + 1)