import sys
sys.stdin = open("4698in.txt",'r')

ToF = [False]*2 + [True]*(10**6+1) # 2까지 소수
PrimeList = []
for i in range(2,10**6+1):
    if not ToF[i]:
        continue
    PrimeList.append(i)
    for j in range(2*i,10**6+1,i):
        if ToF[j]:
            ToF[j] = False

T = int(input())
for Count in range(T):
    D,A,B = map(int,input().split())
    answer = 0
    cnt = 0
    while PrimeList[cnt]<A:
        cnt += 1
    while PrimeList[cnt]<B+1:
        if str(D) in str(PrimeList[cnt]):
            answer += 1
        cnt += 1
        if cnt == len(PrimeList):
            break
    print('#{} {}'.format(Count+1,answer))