import sys
sys.stdin = open("17244in.txt",'r')

import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
li = list(list(x for x in sys.stdin.readline().strip()) for _ in range(m))
ba = []
dy = [-1,0,0,1]
dx = [0,1,-1,0]
y0 = x0 = y1=x0 = 0
ans = 0
def myDist(y,x,desY,desX):
    ba = deque([(y,x,0)])    
    vi = list(list(True for _ in range(n)) for _ in range(m))
    while ba:
        newY,newX,dis = ba.popleft()
        if newY==desY and newX == desX:
            return dis
        for i in range(4):
            checkY = newY + dy[i]
            checkX = newX + dx[i]
            if 0<= checkY<m and 0<= checkX < n and vi[checkY][checkX] and (not li[checkY][checkX]=="#"):
                vi[checkY][checkX] = False
                ba.append((checkY,checkX,dis+1))

def route(y0,x0,cnt,dist):
    global ans
    if cnt == len(ba):
        dist += myDist(y0,x0,y1,x1)
        if ans > dist:
            ans = dist
    else:
        for i in range(len(ba)):
            if viList[i]:
                viList[i] = False
                res = myDist(y0,x0,ba[i][0],ba[i][1])
                route(ba[i][0],ba[i][1],cnt+1,dist+res)
                viList[i] = True

for y in range(m):
    for x in range(n):
        if li[y][x]=="#" or li[y][x]==".":
            pass
        elif li[y][x]=="X":
            ba.append((y,x))
        elif li[y][x]=="S":
            y0 = y
            x0 = x
        elif li[y][x]=="E":
            y1 = y
            x1 = x
ans = 51*51
viList = [True]*(51*51)
route(y0,x0,0,0)
print(ans)