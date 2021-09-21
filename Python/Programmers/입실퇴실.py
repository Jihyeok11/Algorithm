from collections import defaultdict
def solution(enter, leave):
    answer = []
    n = len(enter)
    members = defaultdict(list)
    li = []
    while enter or leave:
        if leave[0] in li:
            li.pop(li.index(leave.pop(0)))
        elif enter:
            member = enter.pop(0)
            for i in li:
                members[member].append(i)
                members[i].append(member)
            li.append(member)
    for i in range(1, n+1):
        answer.append(len(members[i]))
    return answer





print(solution([1,3,2], [1,2,3])) # [0, 1, 1]
print(solution([1, 4, 2, 3], [2, 1, 4, 3])) # [2, 2, 0, 2]
print(solution([3, 2, 1], [1, 3, 2])) # [2, 2, 2]
print(solution([3, 2, 1], [2, 1, 3])) # [1, 1, 2]
print(solution([1, 4, 2, 3], [2, 1, 3, 4])) # [2, 2, 1, 3]