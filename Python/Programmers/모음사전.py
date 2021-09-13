def solution(word):
    answer = 0
    vowel = ["A", "E", "I", "O", "U"]
    cnt = [5**4 + 5**3 + 5 ** 2 + 5 + 1, 5**3 + 5**2 + 5 + 1, 5 ** 2 + 5 + 1, 5 + 1, 1]
    for i in range(len(word)):
        answer += 1
        w = vowel.index(word[i])
        answer += (cnt[i] * w)
    return answer



# print(solution('AAAAE')) # 6
# print(solution('AAAE')) # 10
# print(solution('I')) # 1563
print(solution('EIO')) # 1189