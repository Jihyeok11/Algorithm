def solution(N,K,T):
    T = sorted(T, key=lambda x:(x[0],x[1]))

    print(T)
    cnt = 0
    K_time = [True]*K
    for t in T:
        print(t)
        for i in range(t[0]-1,t[1]):
            if K_time[i]:
                K_time[i] = False
                cnt += 1
                break
    return cnt

print(solution(4,	4,	[[1,3],[1,1],[2,3],[3,4]]))
print(solution(7,	4,	[[1,3],[3,4],[2,4],[2,2],[2,3],[1,2],[1,1] ]))