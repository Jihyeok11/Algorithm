import sys
sys.stdin = open("4615in.txt",'r')

def Othello(X,Y,color):
    # global 
    for i in range(8):
        C_Y = Y + dy[i]
        C_X = X + dx[i]
        if 0<=C_Y<N and 0<= C_X<N and List[C_Y][C_X]!=0 and abs(List[C_Y][C_X]-List[Y][X])==1:
            Sheet = []
            flag = False
            while True:
                Sheet.append((C_Y,C_X))
                C_Y += dy[i]
                C_X += dx[i]
                if not (0<=C_Y<N and  0<=C_X<N) or List[C_Y][C_X]==0:
                    break
                if List[C_Y][C_X]==color:
                    flag = True
                    break
            if flag:
                while Sheet:
                    y,x = Sheet.pop(0)
                    List[y][x] = color
                    pass
            




dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]

T = int(input())
for Count in range(T):
    N,M = map(int,input().split())
    List = [[0 for _ in range(N)] for _ in range(N)]
    List[N//2][N//2-1] = List[N//2 - 1][N//2] = 1
    List[N//2-1][N//2-1] = List[N//2][N//2] = 2
    for _ in range(M):
        X,Y,color = map(int,input().split())
        List[Y-1][X-1] = color
        Othello(X-1,Y-1,color)
    answer1 = 0
    answer2 = 0
    for Y in range(N):
        for X in range(N):
            if List[Y][X] == 1:
                answer1 += 1
            elif List[Y][X] == 2:
                answer2 += 1
    print("#{} {} {}".format(Count+1,answer1, answer2))

    
