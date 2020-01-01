year = int(input())
# months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if year == 1918:
    print('26.09.1918')
elif year < 1918:
    if not year % 4:
        print('12.09.%d' % year)
    else:
        print('13.09.%d' % year)
else:
    if (not year % 4 and year % 100) or not year % 400:
        print('12.09.%d' % year)
    else:
        print('13.09.%d' % year)
