import sys
sys.stdin = open("7662in.txt",'r')

import sys,heapq

def clean(q):
    while q and visited[q[0][1]]==0:
        heapq.heappop(q)

visited = [0] * 1000000
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    hq = []
    lq = []
    push = 0
    pop = 0
    for i in range(n):
        ins,num = sys.stdin.readline().split()
        num = int(num)

        if ins == "I":
            heapq.heappush(hq,(-num,i))
            heapq.heappush(lq,(num,i))
            visited[i] = 1
        else:
            if num == 1:
                clean(hq)
                if hq:
                    visited[hq[0][1]] = 0
                    heapq.heappop(hq)
            else:
                clean(lq)
                if lq:
                    visited[lq[0][1]] = 0
                    heapq.heappop(lq)
    clean(hq)
    clean(lq)

    if hq:
        print(-hq[0][0], lq[0][0])
    else:
        print("EMPTY")