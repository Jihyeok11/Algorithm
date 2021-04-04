import sys
sys.stdin = open("15656in.txt",'r')

N,M = map(int,input().split())
List = sorted(list(map(int,input().split())))
Answer = []
def bubun(idx):
    if idx == M:
        print(*Answer)

    else:
        for i in range(N):
            Answer.append(List[i])
            bubun(idx+1)
            Answer.pop()

bubun(0)