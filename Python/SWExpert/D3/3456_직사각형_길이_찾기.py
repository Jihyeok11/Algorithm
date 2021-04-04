import sys
sys.stdin = open("3456in.txt",'r')

for Count in range(int(input())):
    Number = list(map(int,input().split()))
    A = Number.pop(0)
    B = Number.pop(0)
    C = Number.pop(0)
    if A==B:
        A = C
    elif A == C:
        A = B
    print("#{} {}".format(Count+1,A))

