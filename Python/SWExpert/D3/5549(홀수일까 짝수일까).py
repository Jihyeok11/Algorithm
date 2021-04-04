import sys
sys.stdin = open("5549in.txt",'r')

T = int(input())
for Count in range(T):
    N = float(input())
    if int(N[-1])%2:
        print("#{} Odd".format(Count+1))
    else:
        print("#{} Even".format(Count+1))