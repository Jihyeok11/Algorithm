import sys
sys.stdin = open("2583in.txt",'r')

import sys
Y,X,N = map(int,sys.stdin.readline().split())
li = list(list(0 for _ in range(X)) for _ in range(Y))
v = list(list(True for _ in range(X)) for _ in range(Y))
dy = [-1,1,0,0]
dx = [0,0,-1,1]
for _ in range(N):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            li[y][x]=1
a = []
for y in range(Y):
    for x in range(X):
        if not li[y][x] and v[y][x]:
            cnt = 1
            basket = [(y,x)]
            v[y][x] = False
            while basket:
                newY,newX = basket.pop()
                for i in range(4):
                    checkY = newY + dy[i]
                    checkX = newX + dx[i]
                    if 0<=checkY<Y and 0<= checkX<X and v[checkY][checkX] and not li[checkY][checkX]:
                        cnt += 1
                        v[checkY][checkX] = False
                        basket.append((checkY,checkX))
            a.append(cnt)
a.sort()
print(len(a))
print(*a)