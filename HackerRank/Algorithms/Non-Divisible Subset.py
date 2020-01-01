n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))

# method 1
# counts = [0] * k
# for n in numbers: # frequency list of remainders
#     counts[n % k] += 1

# count = min(counts[0], 1)
# for i in range(1, k//2 + 1):
#     if i != k - i:
#         count += max(counts[i], counts[k-i])
# if k % 2 == 0:
#     count += 1

# print(count)


# method 2
if k == 0 or k == 1:  # speical cases
    print(1)
else:
    output = 0
    mod = [numbers[i] % k for i in range(n)]

    if 0 in mod:  # one 0 can be paired with any other non-divisible number
        output += 1
    mod = [x for x in mod if x != 0]  # delete all 0s

    freq = [0] * k  # frequency table
    for i in range(len(mod)):
        freq[mod[i]] += 1

    index = []
    for i in range(len(freq)):
        maxVal = max(freq)
        maxIndex = freq.index(maxVal)

        if k - maxIndex not in index and maxVal != 0: 
            index.append(maxIndex) # add the most frequent index, since it results in max. output
            if maxIndex*2 % k == 0:
                output += 1
            else:
                output += maxVal
        freq[maxIndex] = 0 # now that we're done with maxIndex, prepare to calculate 2nd maxIndex till every index is set to 0

    print(output)
