import sys
sys.stdin = open("17244in.txt",'r')

import sys
from collections import deque
I = sys.stdin.readline
m,n = map(int,I().split())
k = []
for _ in range(n):
    k.append(list(I().rstrip()))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
fd = dict()
s = 0
t = 0
def bfs(x,y):
    global sx,sy,s
    q = deque()
    q.append((x,y))
    distance = [[0] * m for _ in range(n)]
    distance[x][y] = 1
    tmp = []
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if k[nx][ny] == '#':
                continue
            if k[nx][ny] == '.' and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx,ny))
            if k[nx][ny] == 'X' and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                tmp.append((nx,ny,distance[x][y],fd[(nx,ny)]))

    tmp.sort(key=lambda x:(x[2]-x[3],-x[3],x[2]))
    s += tmp[0][2]
    sx = tmp[0][0]
    sy = tmp[0][1]
    k[sx][sy] = '.'

def from_door(x,y):
    q = deque()
    q.append((x,y))
    distance = [[0] * m for _ in range(n)]
    distance[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if k[nx][ny] == '#':
                continue
            if k[nx][ny] == '.' and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx,ny))
            if k[nx][ny] == 'X' and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx,ny))
                fd[(nx,ny)] = distance[x][y]


def bfs_end(x,y):
    global s
    q = deque()
    q.append((x,y))
    distance = [[0] * m for _ in range(n)]
    distance[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if k[nx][ny] == '#':
                continue
            if k[nx][ny] == '.' and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx,ny))
            if k[nx][ny] == 'E' and distance[nx][ny] == 0:
                s += distance[x][y]
                q.clear()
                break

sx = 0
sy = 0
ex = 0
ey = 0
count = 0

for i in range(n):
    for j in range(m):
        if k[i][j] == 'S':
            k[i][j] = '.'
            sx = i
            sy = j
        elif k[i][j] == 'E':
            ex = i
            ey = j
        elif k[i][j] == 'X':
            count += 1

from_door(ex,ey)
for _ in range(count):
    bfs(sx,sy)
bfs_end(sx,sy)
print(s)