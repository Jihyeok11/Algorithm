from collections import deque
def solution(n, info):
    answer = []
    ba = deque([[n, []]])
    cnt = 0
    while cnt < 11:
        for _ in range(len(ba)):
            arrow, li = ba.popleft()
            if cnt == 10:
                ba.append([0, li + [arrow]])
            else:
                ba.append([arrow, li + [0]])
                res = arrow - info[cnt] - 1
                if res >= 0:
                    ba.append([res, li + [info[cnt] + 1]])
        cnt += 1
    Max = 0
    tp = 0
    for i in ba:
        score = 0
        apeach = 0
        for s in range(11):
            if i[1][s] > info[s]:
                score += (10 - s)
            elif i[1][s] <= info[s] and info[s] > 0:
                apeach += (10 - s)
        gap = score - apeach
        if Max < gap:
            answer = i[1]
            Max = gap
        elif gap > 0 and Max == gap:
            for j in range(10, -1, -1):
                if answer[j] > i[1][j]:
                    break
                elif answer[j] < i[1][j]:
                    answer = i[1]
    if Max:
        return answer
    else:
        return [-1]



print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))