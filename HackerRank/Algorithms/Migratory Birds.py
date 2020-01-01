n = int(input())
data = list(map(int, input().split()))
freq = [0]*5

for i in range(n):
    freq[data[i]-1] += 1

m, t = 0, -1
for i in range(5):
    if freq[i] > m or (freq[i] == m and i < t):
        m = freq[i]
        t = i

print(t+1)
