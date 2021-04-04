import sys
sys.stdin = open("11286in.txt",'r')

import sys,heapq
q = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n:
        heapq.heappush(q,(abs(n),n))
    else:
        if q:
            if len(q)>1:
                a,b = heapq.heappop(q)
                c,d = heapq.heappop(q)
                if a==c:
                    if b>d:
                        print(d)
                        heapq.heappush(q,(a,b))
                    else:
                        print(b)
                        heapq.heappush(q,(c,d))
                else:
                    print(b)
                    heapq.heappush(q,(c,d))
            else:
                a,b = heapq.heappop(q)
                print(b)
        else:
            print(0)