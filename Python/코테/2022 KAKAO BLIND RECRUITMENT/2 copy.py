from collections import defaultdict
vi = defaultdict(bool)
def jinsu(n, q):
    res = ''
    while n > 0:
        n, mod = divmod(n, q)
        res += str(mod)
    return res[::-1] 

def prime(x):
    global vi
    if vi[x]:
        return True
    if x == 1:
        return False
    for i in range(2, x + 1):
        if i != x and not x % i:
            return False
        if vi[i]:
            for j in range(2 * i, x + 1, i):
                vi[j] = False
    return True

def solution(n, k):
    answer = 0
    res = jinsu(n, k)
    cnt = 0
    word = ""
    while cnt < len(res):
        if res[cnt] == "0":
            if word and prime(int(word)):
                answer += 1

            word = ""
        else:
            word += res[cnt]
        cnt += 1
    if word and prime(int(word)):
        answer += 1
                    
    return answer


print(solution(437674, 3))
print()
print(solution(110011, 10))
print()
print(solution(33, 10))
print()
print(solution(37, 10))
print()
print(solution(123495714614282, 10))