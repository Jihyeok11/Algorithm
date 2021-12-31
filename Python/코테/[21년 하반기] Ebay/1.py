import sys
sys.stdin = open("1.txt", 'r')

from collections import defaultdict
answer = 0
vi = list(list(True for _ in range(19)) for _ in range(5))
week = ['MO','TU','WE','TH','FR']

def ts(schedule, t):
    global answer
    if t == 5:
        answer += 1
    else:
        for i in schedule[t]:
            for j in schedule[t]:
                li = j.split(' ')
                if len(li) == 2: # 3시간
                    idx = week.index(li[0])
                    hh, mm = li[1].split(':')
                    time = int(hh) * 2
                    if mm == '30':
                        time += 1
                    time -= 18
                    if not any(vi[idx][time:time+6]):
                        vi[idx]
                        
                else: # 1시간 3분
                    pass
                print(li)
            ts(schedule, t+1)
            

def solution(schedule):
    global answer
    vi = list(range(9, 42))
    ts(schedule, 0)


    return answer


print(solution([['MO 12:00 WE 14:30', 'MO 12:00', 'MO 15:00', 'MO 18:00'], ['TU 09:00', 'TU 10:00', 'TU 15:00', 'TU 18:00'], ['WE 09:00', 'WE 12:00', 'WE 15:00', 'WE 18:00'], ['TH 09:30', 'TH 11:30', 'TH 15:00', 'TH 18:00'], ['FR 15:00', 'FR 15:00', 'FR 15:00', 'FR 15:00']]))