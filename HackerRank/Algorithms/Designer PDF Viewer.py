alphabets = 'abcdefghijklmnopqrstuvwxyz'
heights = list(map(int, input().split()))
letters = input()
max_height = 0

for i in range(len(letters)):
    if max_height < heights[alphabets.index(letters[i])]:
        max_height = heights[alphabets.index(letters[i])]

print(len(letters)*max_height)
