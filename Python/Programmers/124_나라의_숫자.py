def solution(n):
    rule = [0, 1, 2, 4]
    # [0, 1, 2]
    answer = ''
    end = 0 
    cnt = 0
    while True:
        end += 3**(cnt+1)
        if end >= n:
            break
        cnt += 1
    while cnt >= 0:
        r = n//(3**cnt)
        answer += str(rule[r])
        n = n - (r * 3**cnt)
        cnt -= 1
    return answer


print(solution(1)) # 1
print(solution(2)) # 2
print(solution(3)) # 4
# print(solution(4)) # 11
print(solution(9)) # 24

