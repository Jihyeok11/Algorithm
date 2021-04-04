import sys
sys.stdin = open("6019in.txt",'r')

T = int(input())
for Count in range(T):
    D,A,B,F = map(int,input().split())
    T = D/(A+B)
    print("#{} {}".format(Count+1,T*F))