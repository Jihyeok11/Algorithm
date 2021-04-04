import sys
sys.stdin = open("2164in.txt",'r')

import sys
from collections import deque
n = int(sys.stdin.readline())
li = deque(list(range(1,n+1)))
while len(li) > 1:
    li.popleft()
    a = li.popleft()
    li.append(a)
print(li[0])