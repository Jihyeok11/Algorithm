import sys
sys.stdin = open("4012in.txt",'r')

def bubun(idx):
    global Collect, use_check, Check, Min
    
    if idx == N//2:
        SetA = set(Collect)
        SetB = Set - SetA
        RecipeA = 0
        RecipeB = 0
        for j in SetA:
            for k in SetA:
                RecipeA += List[j][k]
        for j in SetB:
            for k in SetB:
                RecipeB += List[j][k]
        if abs(RecipeA - RecipeB) < Min:
            Min = abs(RecipeB - RecipeA)

    else:
        for i in range(N):
            if use_check[i]:
                use_check[i] = False
                Collect.append(i)
                bubun(idx+1)
                use_check[i] = True
                Collect.pop()

T = int(input())
for Count in range(T):
    print("#{0} ".format(Count+1), end= '')

    N = int(input())
    List = [ list(map(int,input().split())) for _ in range(N) ]
    use_check = [True] * N
    Collect = []
    Check = [ i for i in range(N)] #인덱스 값 [0,1,2,3]
    Set = set(Check) # {0,1,2,3}
    Min = 1000
    bubun(0)
    print(Min)