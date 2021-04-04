import sys
sys.stdin = open("15655in.txt",'r')

N,M = map(int,input().split())
List = list(map(int,input().split()))
List.sort()
Answer = []
use_check = [True] * N

def bubun(idx):
    global Answer

    if idx == M:
        print(*Answer)
        return

    else:
        for i in range(idx,N):
            if not use_check[i] :
                continue
            use_check[i] = False
            Answer.append(List[i])
            bubun(idx+1)
            Answer.pop()
            for j in range(i+1,N):
                use_check[j] = True

bubun(0)