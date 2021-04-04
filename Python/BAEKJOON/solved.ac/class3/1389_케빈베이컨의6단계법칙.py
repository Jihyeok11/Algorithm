import sys
sys.stdin = open("1389in.txt",'r')

import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
li = {}
for i in range(1,n+1):
    li[i] = []
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    if not b in li[a]:
        li[a].append(b)
    if not a in li[b]:
        li[b].append(a)
minV = 1000000
ans = 0
for i in range(1,n+1):
    vi = [True] * (n+1)
    vi[i] = False
    ba = deque([])
    res = 0
    for j in li[i]:
        ba.append((j,1))
        vi[j] = False
    while ba:
        a,cnt = ba.popleft()
        res += cnt
        for j in li[a]:
            if vi[j]:
                vi[j] = False
                ba.append((j,cnt+1))
        if res > minV:
            break
    if res < minV:
        minV = res
        ans = i
print(ans)