import sys
sys.stdin = open("16929in.txt",'r')

import sys
n,m = map(int,sys.stdin.readline().split())
li = list(list(x for x in sys.stdin.readline().rstrip()) for _ in range(n))
vi = list([True] * m for _ in range(n))
dy = [1,0,-1,0]
dx = [0,1,0,-1]

def go_round(newY,newX,cnt,color,endY,endX):

    for i in range(4):
        checkY = newY + dy[i]
        checkX = newX + dx[i]
        if 0<= checkY < n and 0 <= checkX < m and li[checkY][checkX]==color and vi[checkY][checkX]:
            vi[checkY][checkX] = False
            if go_round(checkY,checkX,cnt+1,color,endY,endX):
                return True
        elif cnt > 2 and checkY==endY and checkX == endX:
            return True
            

flag = 0
for y in range(n):
    for x in range(m):
        vi = list([True] * m for _ in range(n))
        vi[y][x] = False
        for i in range(4):
            checkY = y + dy[i]
            checkX = x + dx[i]
            if 0<=checkY<n and 0<=checkX < m and vi[checkY][checkX] and li[checkY][checkX]==li[y][x]:
                vi[checkY][checkX] = False
                if go_round(checkY,checkX,1,li[y][x],y,x):
                    flag = 1
                    print("Yes")
                    break
        if flag:
            break
    if flag:
        break
else:
    print("No")