import sys
sys.stdin = open("15666in.txt",'r')

N,M = map(int,input().split())
List = sorted(list(map(int,input().split())))
Answer = []



def bubun(idx):
    if len(Answer) == M:
        print(*Answer)
    else:
        last = 0
        for i in range(idx,N):
            if last != List[i]:
                last = List[i]
                Answer.append(last)
                bubun(i)
                Answer.pop()

bubun(0)