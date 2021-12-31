def palin(P, vi):
    if any(vi):
        for i in range(len(vi)):
            if vi[i]:
                for j in range(i+1, len(vi)):
                    if vi[j]:
                        word1 = P[i] + P[j]
                        word2 = P[j] + P[i]
                        if (word1 == word1[::-1]) or (word2 == word2[::-1]):
                            vi[i] = False
                            vi[j] = False
                            return palin(P, vi)
                        vi[i] = True
                        vi[j] = True
    else:
        return True


def solution(P):
    ans = []
    for k in range(1, len(P)):
        vi = list(True for _ in range(len(P)))
        vi[0] = False
        word1 = P[0] + P[k]
        word2 = P[k] + P[0]
        if (word1 == word1[::-1]) or (word2 == word2[::-1]):
            vi[k] = False
            if palin(P, vi):
                ans.append(P[k])
            vi[k] = True
    return ans



print(solution(['21', '123', '111', '11']))
print(solution(['11', '111', '11', '211']))
