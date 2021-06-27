def solution(n, v1, v2, num, amount):
    answer = 0
    teams = []
    for i in range(n):
        teams.append(set([i+1]))
    for i in range(len(v1)):
        a, b = v1[i], v2[i]
        for team in teams:
            if a in team:
                left = teams.pop(teams.index(team))
                break
        for team in teams:
            if b in team:
                right = teams.pop(teams.index(team))
                break
        teams.append(left | right)
    scores = list(0 for _ in range(len(teams)))
    for i in range(len(num)):
        student = num[i]
        score = amount[i]
        cnt = 0
        for team in teams:
            if student in team:
                scores[cnt] += score
                break
            cnt += 1
    best_team = teams[scores.index(max(scores))]
    print(sorted(best_team)[0]) 
    return answer





solution(10, [1, 10, 6, 5, 6, 9], [3, 7, 2, 8, 7, 3], [3, 4, 5, 1, 8, 7, 9, 2],	[10, 5, 6, -6, -8, 2, -2, 5])
solution(10,	[8, 4, 4, 1],	[1, 10, 9, 4],	[2, 5, 8, 6, 4, 1, 3, 10, 7, 4],	[3, -1, 3, 3, 1, -2, -4, 1, 2, -5])
solution(4,	[1, 3],	[2, 4],	[2, 2],	[1, -2])
solution(6,	[1, 5, 3, 6, 2]	,[5, 4, 6, 2, 3],	[1, 5, 4, 3, 6, 2],	[3, 6, -2, 2, 2, 2])