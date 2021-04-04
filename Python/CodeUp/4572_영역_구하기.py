import sys
sys.stdin = open("in.txt",'r')

sys.setrecursionlimit(10000)
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def area(y,x):
    global total_area
    total_area += 1
    List[y][x] = 1
    for i in range(4):
        newY = y+dy[i]
        newX = x+dx[i]
        if 0<=newY<n and 0<=newX<m and not List[newY][newX]:
            area(newY,newX)


n,m,k = map(int,input().split())
List = [[ 0 for _ in range(m)] for _ in range(n) ]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            if not List[i][j]:
                List[i][j] = 1

answer = 0
basket = []
for Y in range(n):
    for X in range(m):
        if not List[Y][X]:
            answer += 1
            total_area = 0
            area(Y,X)
            basket.append(total_area)
basket.sort()
print(answer)
print(*basket)