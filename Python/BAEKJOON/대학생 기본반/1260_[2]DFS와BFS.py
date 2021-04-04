import sys
sys.stdin = open("1260in.txt",'r')

import sys
from collections import deque
n,m,v = map(int,sys.stdin.readline().split())
ba = {}
for i in range(1,n+1):
    ba[i] = []
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    ba[a].append(b)
    ba[b].append(a)
for i in range(1,n+1):
    ba[i].sort()
lid = [v]
lib = deque([v])
bfs = [v]
dfs = [v]
vid = [True]*(n+1)
vib = [True]*(n+1)
vid[v] = False
vib[v] = False

def my_dfs(l):
    for j in ba[l]:
        if vid[j]:
            vid[j] = False
            dfs.append(j)
            my_dfs(j)

my_dfs(v)
while lib:
    newb = lib.popleft()
    for j in ba[newb]:
        if vib[j]:
            vib[j] = False
            lib.append(j)
            bfs.append(j)
print(*dfs)
print(*bfs)