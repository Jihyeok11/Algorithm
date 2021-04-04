import sys
sys.stdin = open("7576in.txt",'r')

import sys
from collections import deque
m,n = map(int,sys.stdin.readline().split())
li = []
vi = list(list(True for _ in range(m)) for _ in range(n))
zero = 0
dy = [-1,1,0,0]
dx = [0,0,-1,1]
ba = deque([])
for _ in range(n):
    lit = []
    for i in sys.stdin.readline().split():
        a = int(i)
        lit.append(a)
        if not a:
            zero += 1
    li.append(lit)
cnt = time = 0
for y in range(n):
    for x in range(m):
        if li[y][x]==1:
            vi[y][x] = False
            ba.append((y,x))
while ba:
    time += 1
    for _ in range(len(ba)):
        newY,newX = ba.popleft()
        for i in range(4):
            checkY = newY + dy[i]
            checkX = newX + dx[i]
            if 0<= checkY<n and 0<=checkX<m and vi[checkY][checkX] and not li[checkY][checkX]:
                cnt += 1
                ba.append((checkY,checkX))
                vi[checkY][checkX] = False
if zero == cnt:
    print(time-1)
else:
    print(-1)