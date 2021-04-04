import sys
sys.stdin = open("1940in.txt",'r')

T = int(input())
for Count in range(T):
    N = int(input())
    Distance = 0
    V = 0
    for i in range(N):
        Str = input()
        A = int(Str[0])
        if len(Str)>1:
            B = int(Str[2])
        if A==1:
            V += B
            Distance += V
        elif A==2:
            V -= B
            if V <=0:
                V =0
            Distance += V
        elif A==0:
            Distance += V
    print("#{0} {1}".format(Count+1, Distance))