'''
def minion_game(s):
    vowels = 'AEIOU'
    stu, kev = 0, 0
    s_repeat, k_repeat = [], []

    for i in range(len(s)):
        if s[i] in vowels:
            temp = ''
            for j in range(i, len(s)):
                temp += s[j]
                if temp not in k_repeat:
                    k_repeat.append(temp)
                    kev += s.count(temp)
                    # print(temp, s.count(temp))
        else:
            temp = ''
            for j in range(i, len(s)):
                temp += s[j]
                if temp not in s_repeat:
                    s_repeat.append(temp)
                    stu += s.count(temp)

    if stu > kev:
        print('Stuart', stu)
    elif kev > stu:
        print('Kevin', kev)
    else:
        print('Draw')
'''

# take all possible substrings, split them into 2 sets according to starting letter,
# then sum elements, this solution works bc. we are essentially counting every occurences without repeats
def minion_game(s):
    vowels = 'AEIOU'
    kevsc, stusc = 0, 0

    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print('Kevin', kevsc)
    elif kevsc < stusc:
        print('Stuart', stusc)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
