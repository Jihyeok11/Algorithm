import sys
sys.stdin = open("6485in.txt",'r')

T = int(input())
for Count in range(T):
    print("#{} ".format(Count+1),end='')
    N = int(input())
    List = [0 for _ in range(5000)]
    for _ in range(N):
        A,B = map(int,input().split()) #1, 3
        for i in range(A-1,B): #0,1 2
            List[i] += 1
    P = int(input())
    for _ in range(P-1):
        j = int(input())
        print(List[j-1],end=' ')
    j = int(input())
    print(List[j-1])