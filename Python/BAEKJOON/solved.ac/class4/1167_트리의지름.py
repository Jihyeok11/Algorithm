import sys
from collections import deque
sys.stdin= open("1167in.txt",'r')


ba = {}
n = int(sys.stdin.readline().strip())
for _ in range(n):
    li = list(map(int,sys.stdin.readline().split()))
    a = li.pop(0)
    ba[a] = []
    while True:
        b = li.pop(0)
        if not (b==-1):
            c = li.pop(0)
            ba[a].append((b,c))
        else:
            break
