import sys
sys.stdin = open("6692in.txt",'r')

T = int(input())

for Count in range(T):
    N = int(input())
    Salary = 0
    for _ in range(N):
        P,M = map(float,input().split())
        Salary += P*M
    print("#{0} {1:6f}".format(Count+1,Salary))