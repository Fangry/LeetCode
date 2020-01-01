nk = list(map(int, input().split()))
bill = list(map(int, input().split()))
to_check = int(input())

del bill[nk[1]]
actual = sum(bill)/2

if actual == to_check:
    print('Bon Appetit')
elif actual < to_check:
    print(int(to_check-actual))
