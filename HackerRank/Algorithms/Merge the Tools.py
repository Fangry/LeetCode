def merge_the_tools(s, k):
    for i in range(0, len(s), k):
        temp = s[i:i+k]
        output = ''
        for j in range(k):
            if temp[j] not in output:
                output += temp[j]
        print(output)


if __name__ == '__main__':
    s, k = input(), int(input())
    merge_the_tools(s, k)