import sys
sys.stdin = open("1167in.txt",'r')

import sys
from collections import deque

def findU(n):
    vi = [10000] * (n+1)
    ba = [(n,0)]
    while ba:
        idx,leng = ba.pop()

n = int(sys.stdin.readline())
li = list(([0]*(n+1)) for _ in range(n+1))
tree = {}
for _ in range(n):
    line = deque(list(map(int,sys.stdin.readline().split())))
    a = line.popleft() 
    tree[a] = []
    b = line.popleft()
    if b != -1:
        c = line.popleft()
        tree[a].append(b)
        li[a][b] = c
print(tree[1])
print(li)
print(findU(1))