import sys
sys.stdin = open("10200in.txt",'r')

for Count in range(int(input())):
    N,A,B = map(int,input().split())
    print("#{} {} {}".format(Count+1,min(A,B),max(A+B-N,0)))
