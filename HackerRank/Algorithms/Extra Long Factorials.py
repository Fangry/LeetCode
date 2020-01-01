def extraLongFactorials(n):
    if n == 0:
        print(1)
    result = 1
    for i in range(1, n+1):
        result *= i
    print(result)


if __name__ == '__main__':
    extraLongFactorials(int(input()))
