import sys
sys.stdin = open("7562in.txt",'r')

import sys
from collections import deque
for count in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    y1,x1 = map(int,sys.stdin.readline().split())
    y2,x2 = map(int,sys.stdin.readline().split())
    vi = list(list( True for _ in range(n)) for _ in range(n))
    dy = [-2,-2,-1,-1,1,1,2,2]
    dx = [-1,1,-2,2,-2,2,-1,1]
    basket = deque([(y1,x1,0)])
    while basket:
        newY,newX,cnt = basket.popleft()
        if newY == y2 and newX == x2:
            print(cnt)
            break
        for i in range(8):
            checkY = newY + dy[i]
            checkX = newX + dx[i]
            if 0<= checkY < n and 0<=checkX < n and vi[checkY][checkX]:
                vi[checkY][checkX] = False
                basket.append((checkY,checkX,cnt+1))