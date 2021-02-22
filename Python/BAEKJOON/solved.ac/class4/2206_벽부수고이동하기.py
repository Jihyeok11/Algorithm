import sys
from collections import deque
sys.stdin = open("2206in.txt",'r')

dy = [-1,1,0,0]
dx = [0,0,-1,1]
n,m = map(int,sys.stdin.readline().split())
li = list(list( int(x) for x in sys.stdin.readline().strip()) for _ in range(n))
vi = list(list(list(True for _ in range(m)) for _ in range(n)) for _ in range(2))
vi[0][0][0] = False
vi[1][0][0] = False
ba = deque([(0,0,True,0)])
flag = True
while ba:
    newY,newX,rock,cnt = ba.popleft()
    if newY==n-1 and newX==m-1:
        flag = False
        print(cnt+1)
        break
    for i in range(4):
        checkY = newY + dy[i]
        checkX = newX + dx[i]
        if 0<=checkY<n and 0<=checkX<m: # 벽 테스트
            if rock: # 부수기 스킬 있을 때
                if li[checkY][checkX]: # 막혀있으면
                    vi[1][checkY][checkX] = False
                    ba.append((checkY,checkX,False,cnt+1))
                elif not li[checkY][checkX] and vi[0][checkY][checkX]:
                    vi[0][checkY][checkX] = False
                    ba.append((checkY,checkX,True,cnt+1))
            else: # 부수기 스킬 없을 때
                if vi[1][checkY][checkX] and not li[checkY][checkX]:
                    vi[1][checkY][checkX] = False
                    ba.append((checkY,checkX,False,cnt+1))
if flag:
    print(-1)