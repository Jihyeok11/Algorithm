import sys
sys.stdin = open("11279in.txt",'r')

import sys, heapq
lq = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n:
        heapq.heappush(lq,-n)
    else:
        if lq:
            print(-heapq.heappop(lq))
        else:
            print(0)