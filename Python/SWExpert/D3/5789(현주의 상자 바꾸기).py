import sys
sys.stdin = open("5789in.txt",'r')

T = int(input())
for Count in range(T):
    N,Q = map(int,input().split())
    Box = [0]*(N+1)
    for i in range(Q):
        L,R = map(int,input().split())
        for j in range(L,R+1):
            Box[j] = i+1
    Box.pop(0)
    print("#{} ".format(Count+1), end="")
    print(*Box)
