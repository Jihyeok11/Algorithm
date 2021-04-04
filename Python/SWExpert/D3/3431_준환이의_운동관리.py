import sys
sys.stdin = open("3431in.txt",'r')

for Count in range(int(input())):
    L,U,X = map(int,input().split())
    if X>U:
        print("#{} {}".format(Count+1, -1))
    elif L<=X<=U:
        print("#{} {}".format(Count+1, 0))
    elif X<L:
        print("#{} {}".format(Count+1,L-X))