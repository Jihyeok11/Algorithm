def stone(n):
    



    return stone(n-1)

def solution(stones, k):
    answer = ''
    s = 0
    for i in stones:
        s += i
    if s - (len(stones)-1) * k < 0:
        return -1
    answer = stone(len(stones) - 1)
    return answer



print(solution([1, 3, 2], 3))
print(solution([4, 2, 2, 1, 4], 1))
print(solution([5, 7, 2, 4, 9], 20))