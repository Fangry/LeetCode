pattern = re.compile('\B')
matches = pattern.finditer(s)
for match in matches:
    print(match)