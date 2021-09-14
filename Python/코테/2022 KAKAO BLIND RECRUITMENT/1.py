from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    user = defaultdict(list)
    warn = defaultdict(int)
    for i in id_list:
        warn[i]
    for i in report:
        a, b = i.split()
        if not b in user[a]:
            user[a].append(b)
    for i in user:
        for j in user[i]:
            warn[j] += 1
    for i in id_list:
        cnt = 0
        # print(i, user[i])
        for j in user[i]:
            if warn[j] >= k:
                cnt += 1
        answer.append(cnt)
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))