import sys
sys.stdin = open("13460in.txt",'r')

import sys
from collections import deque
# n,m = map(int,sys.stdin.readline().split())
n,m = map(int,input().split())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def go_limit(y,x,dir):
    cnt = 0
    while li[y+dy[dir]][x+dx[dir]] != "#" and li[y][x] != "O":
        y += dy[dir]
        x += dx[dir]
        cnt += 1
    return y,x,cnt
    # while True:
    #     newY = y + dy[dir]
    #     newX = x + dx[dir]
    #     cnt += 1
    #     if 1<= newY <n-1 and 1<= newX < m-1:
    #         if li[newY][newX]==".":
    #             y = newY
    #             x = newX
    #         elif li[newY][newX]=="O":
    #             return newY,newX,cnt
    #         elif li[newY][newX]=="#":
    #             return y,x,cnt
    #     else:
    #         return y,x,cnt

def myround(ry,rx,by,bx):
    ba = deque([(ry,rx,by,bx,0)])
    vi[ry][rx][by][bx] = False
    while ba:
        newRY,newRX,newBY,newBX,cnt = ba.popleft()
        if cnt >= 10:
            return -1
        for i in range(4):
            checkRY,checkRX,cntR = go_limit(newRY,newRX,i)
            checkBY,checkBX,cntB = go_limit(newBY,newBX,i)
            if li[checkBY][checkBX] != "O":
                if li[checkRY][checkRX]=="O":
                    return cnt+1
                
                if checkRY==checkBY and checkRX==checkBX:
                    if cntR > cntB:
                        checkRY -= dy[i]
                        checkRX -= dx[i]
                    else:
                        checkBY -= dy[i]
                        checkBX -= dx[i]
                
                if vi[checkRY][checkRX][checkBY][checkBX]:
                    vi[checkRY][checkRX][checkBY][checkBX] = False
                    ba.append((checkRY,checkRX,checkBY,checkBX,cnt+1))
    return -1

li = list(list(x for x in sys.stdin.readline().strip()) for _ in range(n))
ry = rx = by = bx = 0
for y in range(n):
    for x in range(m):
        if li[y][x] == "R":
            ry,rx = y,x
        elif li[y][x] == "B":
            by,bx = y,x
# vi = list(list(list(list(True for _ in range(m)) for _ in range(n)) for _ in range(m)) for _ in range(n))
vi = [[[[True] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
print(myround(ry,rx,by,bx))