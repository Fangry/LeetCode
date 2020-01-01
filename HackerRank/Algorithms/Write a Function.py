year = int(input())

def is_leap(year):
    output = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                output = True
        else:
            output = True
    return output

print(is_leap(year))