def compareTriplets(a, b):
    output = [0,0]
    for i in range(3):
        if a[i] > b[i]:
            output[0] += 1
        elif a[i] < b[i]:
            output[1] += 1
    return output

