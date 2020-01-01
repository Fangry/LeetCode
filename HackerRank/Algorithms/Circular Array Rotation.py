n, k, q = list(map(int, input().split()))
arr = list(map(int, input().split()))
r = k % n

for i in range(q):
    m = int(input())
    print(arr[(n - r + m) % n]) # remember inside [] computes the index and not the value
    
