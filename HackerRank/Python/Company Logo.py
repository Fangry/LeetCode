# the trick to this question is to sort by the tiebreaking rule (alphabetical order) 1st then
# by the primary rule that is the character count

s = input()
count = {}

for c in s:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

i = 0
count2 = sorted(count.items(), key=lambda item: item[0])
count3 = sorted(count2, key=lambda item: item[1], reverse=True)

for t in count3:
    if i < 3:
        print(t[0], t[1], sep=' ')
        i += 1
    else:
        break

