import sys

def solution(routes):
    answer = 1
    routes.sort()
    end = start = -30001
    cnt = 0
    for i in routes:
        if end < i[0]:
            start = i[0]
            end = i[1]
            answer += cnt
            cnt = 1
        elif start <= i[0] and i[1] <= end:
            start = i[0]
            end = i[1]
        elif i[0]<= end and end < i[1]:
            start = i[0]


    return answer


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))