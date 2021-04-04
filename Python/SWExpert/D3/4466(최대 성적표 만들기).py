import sys
sys.stdin = open("4466in.txt",'r')

T = int(input())
for Count in range(T):
    N,K = map(int,input().split())
    Score = list(map(int,input().split()))
    Score.sort()
    total = 0
    for _ in range(K):
        total += Score.pop()
    print("#{} {}".format(Count+1,total))