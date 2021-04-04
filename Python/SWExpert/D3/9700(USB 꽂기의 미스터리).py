import sys
sys.stdin = open("9700in.txt",'r')

T = int(input())
for Count in range(T):
    p, q = map(float,input().split())
    S1 = (1-p)*p*q
    S2 = p*(1-q)*q
    if S1<S2:
        print("#{} YES".format(Count+1))
    else:
        print("#{} NO".format(Count+1))