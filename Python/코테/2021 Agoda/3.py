import sys
sys.stdin = open("3in.txt",'r')
from collections import deque
n,m = map(int,input().split())
ba = deque([0])
answer = 0
for _ in range(m-1):
    a, b = map(int,input().split())
    for _ in range(len(ba)):
        c = ba.popleft()
        for i in range(a, b+1):
            r = c+i
            if n >= r:
                ba.append(c+i)
a,b = map(int,input().split())
for _ in range(len(ba)):
    c = ba.popleft()
    for i in range(a,b+1):
        if c+i == n:
            answer += 1
print(answer)