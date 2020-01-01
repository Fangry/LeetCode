for i in range(int(input())):
    s = input()
    d = int(s)
    count = 0
    for j in range(len(s)):
        if s[j] != '0' and d % int(s[j]) == 0:
            count += 1
    print(count)
