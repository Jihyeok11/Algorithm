import sys
sys.stdin = open("7576in.txt",'r')

from collections import deque
dy = [-1,1,0,0]
dx = [0,0,-1,1]
M,N = map(int,input().split())
boxes = []
tomato = deque([])
visited = list(list(True for _ in range(M)) for _ in range(N))
check = 0
for y in range(N):
    List = list(map(int,input().split()))
    boxes.append([])
    for x in range(len(List)):
        if List[x] == 1:
            tomato.append((y,x,0))
        boxes[y].append(List[x])
        if List[x] == -1:
            check += 1
lastday = 0
while tomato:
    newY,newX,day = tomato.popleft()
    check += 1
    for i in range(4):
        pointY = newY + dy[i]
        pointX = newX + dx[i]
        if 0<= pointY < N and 0 <= pointX < M and visited[pointY][pointX] and boxes[pointY][pointX]==0:
            visited[pointY][pointX] = False
            tomato.append((pointY,pointX,day+1))
            
    if day > lastday:
        lastday = day
if N*M == check:
    print(lastday)
else:
    print(-1)