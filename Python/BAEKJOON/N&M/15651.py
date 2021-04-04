import sys
sys.stdin = open('15651in.txt','r')

N,M = map(int,input().split())
List = []
for i in range(N):
    List.append(i+1)
Answer = []
def bubun(idx):
    global Answer
    if idx == M:
        print(*Answer)
    else:
        for i in range(N):
            Answer.append(List[i])
            bubun(idx+1)
            Answer.pop()

bubun(0)