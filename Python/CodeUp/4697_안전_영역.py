import sys
sys.stdin = open("in.txt",'r')


sys.setrecursionlimit(3000)
N = int(input())
Max = 0
Min = 100000
List = []
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def Miro(Y,X,water):
    global visited
    visited[Y][X] = False
    for i in range(4):
        newY = Y + dy[i]
        newX = X + dx[i]
        if 0<=newY<N and 0<=newX<N and List[newY][newX] > water and visited[newY][newX]:
            Miro(newY,newX,water)

for _ in range(N):
    puts = []
    got = map(int,input().split())
    for some in got:
        if Max < some:
            Max = some
        elif Min > some:
            Min = some
        puts.append(some)
    List.append(puts)
# print(List)
landMax = 0
for water in range(Min,Max):
    visited = [ [ True for _ in range(N)] for _ in range(N) ]
    # water = min~max
    lands = 0
    for Y in range(N):
        for X in range(N):
            if List[Y][X] > water and visited[Y][X]:
                lands += 1
                Miro(Y,X,water)
    if lands > landMax:
        landMax = lands
    # print(0)
print(max(landMax,1))


