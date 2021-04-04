import sys
sys.stdin = open("1167in.txt",'r')

import sys
from collections import deque

def findU(idx):
    global cnt
    ba = deque(cn[idx]) # [3]
    bowl = [idx]
    for i in cn[idx]:
        bowl.append(i) 
    while ba:
        new = ba.popleft()
        for i in cn[new]:
            if not i in bowl: # [4]
                bowl.append(i)
                ba.append(i)
                res = min(li[idx][i], li[idx][new] + li[new][i])
                li[idx][i] = res
                li[i][idx] = res

n = int(sys.stdin.readline())
li = list(([1000]*(n+1)) for _ in range(n+1))
cn = {}
for _ in range(n):
    ba = deque(list(map(int,sys.stdin.readline().split())))
    a = ba.popleft()
    li[a][a] = 0
    cn[a] = []
    while True:
        b = ba.popleft()
        if b != -1:
            cn[a].append(b)
            c = ba.popleft()
            li[a][b] = c
        else:
            break
for i in range(1,n+1):
    findU(i)
ans = 0
for i in range(1,n+1):
    ans = max(ans,max(li[i][1:]))
print(ans)