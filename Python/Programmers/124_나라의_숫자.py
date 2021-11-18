import math
def solution(n):
    num = [4, 1, 2]
    answer = ''
    li = []
    cnt = 1
    while n > 0:
        tp = 3 ** cnt
        li.append(num[math.ceil(((n % tp) / tp)*3)])
        n -= tp
        cnt += 1
    print(li)
            
    return answer
print(solution(1)) # 1
print(solution(2)) # 2
print(solution(3)) # 4
# print(solution(4)) # 11
print(solution(9)) # 24
print(solution(83))
