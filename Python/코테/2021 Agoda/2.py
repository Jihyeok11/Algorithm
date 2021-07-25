import sys
sys.stdin = open("2in.txt",'r')
months = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
days = {}
for _ in range(int(input())):
    inDay, outDay = input().split()
    id_y, id_m, id_d = map(int,inDay.split('-'))
    od_y, od_m, od_d = map(int,outDay.split('-'))
    start_day = (id_y - 1) * 365 + months[id_m] + id_d
    end_day = (od_y - 1) * 365 + months[od_m] + od_d
    for day in range(start_day, end_day):
        if day in days:
            days[day] += 1
        else:
            days[day] = 1
maxdays = 0
answerday = 0
a_year = a_month = a_day = 0
for key, val in days.items():
    if val > maxdays:
        maxdays = val
        answerday = key
a_year = answerday // 365
a_day = answerday - a_year * 365
if not a_day:
    a_year -= 1
    a_month = 12
    a_day = 31
else:
    for i in range(1,13):
        if a_day > months[i]:
            a_month += 1
            a_day -= months[i]
        else:
            break
year = str(a_year+1)
if a_month < 10:
    month = "0"+str(a_month)
else:
    month = str(a_month)
if a_day < 10:
    day = "0"+str(a_day)
else:
    day = str(a_day)
print(days)
print("{}-{}-{}".format(year, month, day))
