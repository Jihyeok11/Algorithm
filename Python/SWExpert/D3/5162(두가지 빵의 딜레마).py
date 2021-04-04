import sys
sys.stdin = open("5162in.txt",'r')

T = int(input())
for Count in range(T):
    A,B,C = map(int,input().split())
    D = min(A,B)
    print("#{} {}".format(Count+1,C//D))


