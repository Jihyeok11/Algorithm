import sys
sys.stdin = open('15650in.txt','r')
N,M = map(int,input().split())
use_check = [True] * N
Numbers = []
List = []
for i in range(N):
    List.append(i+1)


def bubun(idx):
    global use_check,Numbers
    if idx==M:
        print(*Numbers)
        return

    for i in range(idx,N):
        if not use_check[i]:
            continue
        use_check[i] = False
        Numbers.append(List[i])
        bubun(idx+1)
        Numbers.pop()
        for j in range(i+1,N):
            use_check[j] = True
bubun(0)
