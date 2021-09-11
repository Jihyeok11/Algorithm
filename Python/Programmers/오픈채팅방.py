from collections import defaultdict
def solution(record):
    answer = []
    user = defaultdict(str)
    for i in record:
        s = i.split()
        if s[0] == "Enter" or s[0] == "Change":
            user[s[1]] = s[2]
            answer.append(s[1]+"님이 들어왔습니다.")
        elif s[0] == "Leave":
            answer.append(s[1]+"님이 나갔습니다.")
    for i in range(len(answer)):
        idx = answer[i].find("님")
        tp = user[answer[i][:idx]]
        right = answer[i][idx:]
        answer[i] = tp + right
    return answer





print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))