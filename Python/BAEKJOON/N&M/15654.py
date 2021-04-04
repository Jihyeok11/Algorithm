import sys
sys.stdin = open("15654in.txt",'r')

N,M = map(int,input().split())
List = list(map(int,input().split()))
List.sort()
use_check = [True]*N
Answer = []

def bubun(idx):
    global Answer
    
    if idx ==M:
        print(*Answer)

    else:

        for i in range(N):
            if use_check[i]:
                use_check[i] = False
                Answer.append(List[i])
                bubun(idx+1)A
                Answer.pop()
                use_check[i] = True
            
bubun(0)