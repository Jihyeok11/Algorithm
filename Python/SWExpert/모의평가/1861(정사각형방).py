import sys
sys.stdin = open('1861in.txt','r')

def iswall(Y,X):
    if Y<0 or X<0 or Y>= N or X>=N:
        return True
    return False

def Miro(Y,X):
    global count
    dy = [0,0,-1,1]
    dx = [-1,1,0,0]
    for i in range(4):
        C_Y = Y+dy[i]
        C_X = X+dx[i]
        if (iswall(C_Y,C_X) == False) and (List[C_Y][C_X] - List[Y][X] ==1):
            count += 1
            Miro(C_Y, C_X)

T = int(input())
for Count in range(T):
    print("#{} ".format(Count+1),end='')
    N = int(input())
    List = [list(map(int,input().split())) for _ in range(N)]
    Max_Count = 0
    Answer = []
    for Y in range(N):
        for X in range(N):
            count = 1
            Miro(Y,X)
            if Max_Count < count:
                Max_Count = count
                Answer= [List[Y][X]]
            if Max_Count == count:
                Max_Count = count
                Answer.append(List[Y][X])
    print(min(Answer),end=' ')
    print( Max_Count)