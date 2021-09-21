def solution(weights, head2head):
    answer = []
    ranks = []
    rates = []
    for i in range(len(head2head)):
        cnt = 0
        for j in range(len(head2head[i])):
            if head2head[i][j] == "W" and weights[i] < weights[j]:
                cnt += 1
        if head2head[i].count("W") or head2head[i].count("L"):
            ranks.append([(head2head[i].count("W")) / (head2head[i].count("W") + head2head[i].count("L")) * 100, cnt, weights[i], i])
        else:
            ranks.append([0, cnt, weights[i], i])
    ranks = sorted(ranks, key=lambda x: (-x[0], -x[1], -x[2], x[3] ))
    for i in ranks:
        answer.append(i[3] + 1)
    return answer



print(solution([60, 70, 60], ["NNN", "NNN", "NNN"])) # [2, 1, 3]
print(solution([145, 92, 86], ["NLW", "WNL", "LWN"])) # [2, 3, 1]
print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"])) # [3, 4, 1, 2]