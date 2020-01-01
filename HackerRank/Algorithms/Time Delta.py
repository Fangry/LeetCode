from datetime import datetime

for i in range(int(input())):
    date1, date2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z'), datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(int(abs(date1-date2).total_seconds()))
