import sys, bisect
from collections import deque
sys.stdin = open("2075in.txt",'r')

n = int(sys.stdin.readline())
ans = deque([-10**8] * n)
for _ in range(n):
    for i in list(map(int, sys.stdin.readline().strip().split())):
        bisect.insort(ans, i)
        ans.popleft()
print(ans[0])