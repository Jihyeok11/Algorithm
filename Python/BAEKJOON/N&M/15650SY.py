import sys
sys.stdin = open('15650in.txt','r')

N, M = map(int, input().split())
 
Numbers = []
 
def bubun(idx):
    if len(Numbers) == M:
        print(*Numbers)
        return
    for i in range(idx + 1, N + 1):
        Numbers.append(i)
        bubun(i)
        Numbers.pop()
 
bubun(0)