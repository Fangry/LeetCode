n, d = list(map(int, input().split()))
nums = list(map(int, input().split()))
output = 0

for i in range(n):
    if nums[i] + d in nums and nums[i] + 2*d in nums:
        output += 1

print(output)
