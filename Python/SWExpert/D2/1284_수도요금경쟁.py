import sys
sys.stdin = open("1284in.txt",'r')

T = int(input())
for Count in range(T):
    P,Q,R,S,W = map(int,input().split())
    
    Price_A = P * W
    Price_B = 0
    if W<=R:
        Price_B = Q
    elif W>R: 
        Price_B = Q + (W-R)*S
    print("#{0} {1}".format(Count+1, min(Price_A,Price_B)))