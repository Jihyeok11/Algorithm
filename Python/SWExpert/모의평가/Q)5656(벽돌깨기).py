import sys
sys.stdin = open("5656in.txt",'r')

def shoot(List,idx,p):
    Copy = List[:]
    if idx == N:
        for i in p:
            boomb(i, List,N,W,H)
            List = Copy[:]
        pass

    else:
        for i in range(W):
            p[idx] = i
            shoot(List,idx+1,p)

def boomb(X, List, N, W, H):
    
    Y = 0
    while Y <H and List[Y][X] ==0:
        Y += 1
    q = []
    idx = List[Y][X]
    q.append((Y,X))
    while len(q) != 0:
        Y,X = q.pop(0)
        idx = List[Y][X]
        List[Y][X] = 0
        for i in range(1,idx):
            for j in range(4):
                C_Y = Y + i * dy[j]
                C_X = X + i * dx[j]
                if 0 <= C_Y < H and 0 <= C_X < W:
                    q.append((C_Y,C_X))
            
            


dy = [0,0,-1,1]
dx = [1,-1,0,0]

T = int(input())
for Count in range(T):
    N,W,H = map(int,input().split())
    List = [ list(map(int,input().split())) for _ in range(H) ]
    p = [ 0 for _ in range(N)] # p = [0,0,0]
    shoot(List,0,p)