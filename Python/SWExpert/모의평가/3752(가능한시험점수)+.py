import sys
sys.stdin = open("3752in.txt",'r')


T = int(input())
for Count in range(T):
    N = int(input())
    List = list(map(int,input().split()))
    Sum = sum(List)
    p = [0 for _ in range(Sum+1)]
    p[0] = 1
    for i in List: #i = 2,3,5
        for j in range(Sum,i-1,-1): #j = 2~10, 3~10
            if p[j-i]:
                p[j] = 1
    print("#{0} {1}".format(Count+1, p.count(1)))