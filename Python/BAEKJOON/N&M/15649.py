import sys
sys.stdin = open("15649in.txt",'r')    


N,M = map(int,input().split())
List = []
for i in range(N):
    List.append(i+1)

use_check = [True] * N
check = [0 for _ in range(N)]
Answer = []
def bubun(idx):
    if idx==M:
        print(*Answer)
        return
    else:
        for i in range(N):
            if not use_check[i]:
                continue
            use_check[i] = False
            Answer.append(List[i])
            bubun(idx+1)
            Answer.pop()
            use_check[i] = True

bubun(0)

