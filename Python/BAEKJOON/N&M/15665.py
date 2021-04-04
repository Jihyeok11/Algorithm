import sys
sys.stdin = open("15665in.txt",'r')




N,M = map(int,input().split())
List  = sorted(list(map(int,input().split())))

Answer = []

def bubun(idx):
    if len(Answer) == M:
        print(*Answer)

    else:
        last = 0
        for i in range(N):
            if last != List[i]:
                last = List[i]
                Answer.append(last)
                bubun(idx+1)
                Answer.pop()
bubun(0)