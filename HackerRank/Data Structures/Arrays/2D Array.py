grid = [list(map(int, input().split())) for i in range(6)]
maxNum = -9 * 6 * 6

for i in range(4):
    for j in range(4):
        temp = grid[i][j] + grid[i][j+1] + grid[i][j+2] + \
            grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
        if temp > maxNum:
            maxNum = temp

# print(grid)
print(maxNum)
