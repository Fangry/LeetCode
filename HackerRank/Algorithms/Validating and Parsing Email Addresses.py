import re

for i in range(int(input())):
    email = input()
    if re.match(r'<[a-zA-Z0-9][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>', email.split(' ')[1]):
        print(email)
