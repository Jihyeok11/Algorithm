import sys
sys.stdin = open("16236in.txt",'r')

import sys
from collections import deque
dy = [-1,0,1,0]
dx = [0,-1,0,1]

def eat(sy,sx):
    global lv,eats,time
    vi = list(list(True for _ in range(n)) for _ in range(n))
    vi[sy][sx] = False
    ba = deque([(sy,sx,0)])
    ly = lx = 25
    leng = 1000
    while ba:
        newY,newX,cnt = ba.popleft()
        if leng < cnt+1:
            continue
        for i in range(4):
            checkY = newY+dy[i]
            checkX = newX+dx[i]
            if 0 <= checkY < n and 0 <= checkX < n and vi[checkY][checkX]:
                vi[checkY][checkX] = False
                if li[checkY][checkX] and lv >li[checkY][checkX] :
                    if checkY < ly:
                        ly,lx,leng = checkY,checkX,cnt+1
                    elif checkY == ly and checkX < lx:
                        lx,leng = checkX,cnt+1
                elif (not li[checkY][checkX]) or lv==li[checkY][checkX]:
                    ba.append((checkY,checkX,cnt+1))
    if leng != 1000:
        li[ly][lx] = 0
        eats += 1
        if lv == eats:
            lv += 1
            eats = 0
        time += leng
        eat(ly,lx)

n = int(sys.stdin.readline())
li = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
sy = sx = flag= 0
for y in range(n):
    for x in range(n):
        if li[y][x] ==9:
            sy,sx = y,x
            li[y][x] = 0
            flag = 1
            break
    if flag:
        break
lv = 2
eats = 0
time = 0
eat(sy,sx)
print(time)