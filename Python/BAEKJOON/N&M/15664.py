import sys
sys.stdin = open("15664in.txt",'r')

N,M = map(int,input().split())
List = sorted(list(map(int,input().split())))
use_check = [True] * N
Answer = []
def bubun(idx):
    if len(Answer) == M:
        print(*Answer)

    else:
        last = 0
        for i in range(idx,N):
            if use_check[i] and last != List[i]:
                use_check[i] = False
                last = List[i]
                Answer.append(List[i])
                bubun(i+1)
                Answer.pop()
                use_check[i] = True

bubun(0)