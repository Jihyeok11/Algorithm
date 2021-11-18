def solution(n):
    num = [1, 2, 4]
    answer = ''
    li = []
    if n <= 3:
        answer = num[n-1]
    else:
        tp = num[(n % 3) - 1]
        while n:
            li.append(n % 3)
            n //= 3
        for i in range(len(li)-1, -1, -1):
            answer += str(num[li[i]-1])
            
    return answer
print(solution(1)) # 1
print(solution(2)) # 2
print(solution(3)) # 4
# print(solution(4)) # 11
print(solution(9)) # 24
print(solution(83))
