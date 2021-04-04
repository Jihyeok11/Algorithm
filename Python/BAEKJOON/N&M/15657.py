import sys
sys.stdin = open("15657in.txt",'r')

N,M = map(int,input().split())
List = sorted(list(map(int,input().split())))
Answer = []
def bubun(idx):
    if len(Answer) == M:
        print(*Answer)

    else:
        for i in range(idx,N):
            Answer.append(List[i])
            bubun(idx)
            Answer.pop()
            idx += 1
            
bubun(0)