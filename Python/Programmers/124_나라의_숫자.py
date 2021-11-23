def solution(n):
    if n<=3:
        return '124'[n-1]
    q, r = divmod(n-1, 3)
    return solution(q) + '124'[r]
print(solution(1)) # 1
print(solution(2)) # 2
print(solution(3)) # 4
# print(solution(4)) # 11
print(solution(9)) # 24
print(solution(83)) # 2242