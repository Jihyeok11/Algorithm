def solution(n, k, bulbs):
    answer = 0
    li = [0] * n
    for i in range(len(bulbs)):
        if bulbs[i] == 'B':
            li[i] = 2
        elif bulbs[i] == 'G':
            li[i] = 1
    for i in range(n):
        if n-i < k:
            break
        if li[i]:
            cnt = 3 - li[i]
            answer += cnt
            for j in range(i, i+k):
                li[j] = (li[j] + cnt) % 3
    if sum(li):
        return -1

    return answer



print(solution(6, 3, "RBGRGB")) # 3
print(solution(3, 2, "BGG")) # -1
print(solution(4, 2, "GBBG")) # 6