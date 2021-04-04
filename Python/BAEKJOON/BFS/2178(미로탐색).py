import sys
sys.stdin = open("2178in.txt",'r')

N, M = map(int,input().split())
List = [[ int(x) for x in input()] for _ in range(N)]
Visited = [[0 for _ in range(M)] for _ in range(N)]
dy = [0,0,-1,1]
dx = [-1,1,0,0]
X = Y = 0
Cnt = 1
Queue = [(Y,X,Cnt)]
Visited[Y][X] = 1
def Maze(Queue,Cnt):
    while Queue:
        Y,X,Cnt = Queue.pop(0)
        for i in range(4):
            C_Y = Y + dy[i]
            C_X = X + dx[i]
            if 0<=C_X<M and 0<=C_Y<N and List[C_Y][C_X] and Visited[C_Y][C_X]==0:
                Visited[C_Y][C_X] = Cnt + 1
                Queue.append((C_Y,C_X,Cnt+1))
        

Maze(Queue,Cnt)
print(Visited[-1][-1])