# vi = [False, False]

def jinsu(n, q):
    res = ''
    while n > 0:
        n, mod = divmod(n, q)
        res += str(mod)
    return res[::-1] 
def prime(x):
    for i in range(2, x):
        if not x % i:
            return False
    return True
def solution(n, k):
    answer = 0
    res = jinsu(n, k)
    if not "0" in res:
        # vi += list(True for _ in range(int(res) - 1))
        if prime(int(res)):
            answer += 1
    else:
        cnt = 0
        word = ""
        while cnt < len(res):
            if res[cnt] == "0":
                if word and prime(int(word)):
                    answer += 1
                    # vi += list(True for _ in range(int(word) - (len(vi) - 1)))

                    # for i in range(2, int(word) + 1):
                    #     if vi[i]:
                    #         if not int(word) % i:
                    #             vi[i] = False
                    #             break
                    #         for j in range(2 * i, int(word) + 1, i):
                    #             vi[j] = False
                    #     if vi[int(word)] != False:
                    #         break
                # if word and vi[int(word)]:
                #     answer += 1
                word = ""
            else:
                word += res[cnt]
            cnt += 1
        if word:
            if prime(int(word)):
                answer += 1
            # if len(vi) - 1 < int(word):
            #     vi += list(True for _ in range(int(word) - (len(vi) - 1)))
            #     for i in range(2, int(word) + 1):
            #         if vi[i]:
            #             for j in range(2 * i, int(word) + 1, i):
            #                 vi[j] = False
            #         if vi[int(word)] != False:
            #             break
            # if vi[int(word)]:
            #     answer += 1
        
    return answer


print(solution(437674, 3))
print()
print(jinsu(1000000, 3))
print(solution(110011, 10))
print()
print(solution(33, 10))
print()
print(solution(37, 10))
print()
print(solution(112211211001, 10))