import sys
sys.stdin = open("2493in.txt",'r')

from collections import deque
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().strip().split()))
answer = list(0 for _ in range(n))
top = deque([(n-1, li[n-1])])
for i in range(n-2, -1, -1):
    for _ in range(len(top)):
        t = top.popleft()
        if t[1] < li[i]:
            topFlag = 0
            answer[t[0]] = i
        else:
            top.append(t)
    top.append((i, li[i]))
        
print(*answer)