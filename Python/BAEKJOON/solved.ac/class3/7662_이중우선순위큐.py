import sys
sys.stdin = open("7662in.txt",'r')

import sys, heapq

def clear(q):
    while q and vi[q[0][1]]:
        heapq.heappop(q)

for _ in range(int(sys.stdin.readline())):
    lq = []
    hq = []
    # vi = [True] * 1000000
    vi = [True] * 30
    for i in range(int(sys.stdin.readline())):
        a,b = sys.stdin.readline().split()
        b = int(b)
        if a=="I":
            heapq.heappush(lq,(b,i))
            heapq.heappush(hq,(-b,i))
            vi[i] = False
        else:
            if b==1:
                clear(hq)
                if hq:
                    vi[hq[0][1]] = True
            else:
                clear(lq)
                if lq:
                    vi[lq[0][1]] = True
    clear(hq)
    clear(lq)
    if hq:
        print(-hq[0][0],lq[0][0])
    else:
        print("EMPTY")