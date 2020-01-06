def swap_case(s):
    result = ''
    for c in s:
        if c.isalpha() and c.isupper():
            result += c.lower()
        elif c.isalpha() and c.islower():
            result += c.upper()
        else:
            result += c
            
    return result