n, nums = int(input()), list(map(int, input().split()))
print(any(map(lambda k: str(k) == str(k)[::-1], nums))) if all(list(map(lambda x: x > 0, nums))) else print(False)


  
