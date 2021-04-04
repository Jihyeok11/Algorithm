import sys
sys.stdin = open("6057in.txt",'r')


def Tri(start, Cnt, End):
    global Answer
    if Cnt >= 3:
        return 
    for l in range(len(Dict[End])):
        if Cnt < 2 and Dict[End][l] > End:
            Tri(start, Cnt+1,Dict[End][l])
        if Cnt==2 and Dict[End][l]==start:
            Answer += 1
            return 
    return 


T = int(input())

for Count in range(T):
    N,M = map(int,input().split())
    Dict = {} # {1: [2, 3], 2: [1, 3], 3: [2, 1]}
    for i in range(1,N+1):
        Dict[i] = []
    for i in range(M):
        start, end = map(int,input().split())
        Dict[start] += [end]
        Dict[end] += [start]
    Answer = 0
    for i in range(N):
        for j in range(len(Dict[i+1])):
            if i+1 < Dict[i+1][j]:
                Tri(i+1,1,Dict[i+1][j]) # (1,0,2)
    print("#{} {}".format(Count+1,Answer))