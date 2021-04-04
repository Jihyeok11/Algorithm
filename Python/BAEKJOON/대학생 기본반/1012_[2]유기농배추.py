import sys
sys.stdin = open("1012in.txt",'r')

import sys

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bug(Y,X):
    basket = [(Y,X)]
    while basket:
        newY,newX = basket.pop()
        for i in range(4):
            checkY = newY+dy[i]
            checkX = newX+dx[i]
            if 0<= checkY < y and 0<= checkX < x and visited[checkY][checkX] and land[checkY][checkX]:
                visited[checkY][checkX] = False
                basket.append((checkY,checkX))

for count in range(int(sys.stdin.readline())):
    x,y,k = map(int,sys.stdin.readline().split())
    land = list(list(0 for _ in range(x)) for _ in range(y))
    for _ in range(k):
        X,Y = map(int,sys.stdin.readline().split())
        land[Y][X] = 1
    visited = list(list(True for _ in range(x)) for _ in range(y))
    answer = 0
    for a in range(y):
        for b in range(x):
            if land[a][b] and visited[a][b]:
                visited[a][b] = False
                answer += 1
                bug(a,b)
    print(answer)