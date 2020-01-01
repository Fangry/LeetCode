import re

for i in range(int(input())):
    findings = re.findall(r'([\s:])(#[a-fA-F0-9]{3,6})', input())
    for j in findings:
        print(j[1])

