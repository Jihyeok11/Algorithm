import copy,sys
sys.stdin = open("4697in.txt",'r')
    
dy = [0,0,-1,1]
dx = [-1,1,0,0]

def Sink(Y,X):
    global F_List, rain

    while len(Rain_spot):
        Y,X = Rain_spot.pop()
        
        for i in range(4):
            C_Y = Y+dy[i]
            C_X = X+dx[i]
            if 0<=C_Y<N and 0<=C_X<N and F_List[C_Y][C_X] >rain:
                Rain_spot.append((C_Y,C_X))
                F_List[C_Y][C_X] = 0


N = int(input())
List = [list(map(int,input().split())) for _ in range(N)]


Rain = []
for Y in range(N):
    for X in range(N):
        if List[Y][X] not in Rain: 
            Rain.append(List[Y][X])


Answer = [] 
AAnswer=[]
Max = 1
for rain in Rain: #6, 8, 2, 3, 4, 7, 5, 
    F_List = copy.deepcopy(List)
    Cnt = 0 # 안전 지역 개수
    for Y in range(N):
        for X in range(N):

            if F_List[Y][X] > rain:
                Rain_spot = [(Y,X)]
                AAnswer.append((Y,X))
                F_List[Y][X] = 0
                Cnt += 1
                Sink(Y,X)
            else:
                F_List[Y][X] = 0
    Answer.append(Cnt)
    if Cnt > Max:
        Max = Cnt
    print((AAnswer))
print(Answer+[1])