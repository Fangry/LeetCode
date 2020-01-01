n = int(input())
a = sorted(list(map(int, input().split())))
freq = [0]*100
maxi = 0

for i in range(n):
    freq[a[i]] += 1

for i in range(99):
    if freq[i] + freq[i+1] > maxi:
        maxi = freq[i] + freq[i+1]

print(maxi)
