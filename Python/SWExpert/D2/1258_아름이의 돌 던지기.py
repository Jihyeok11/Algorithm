import sys
sys.stdin = open("1258in.txt",'r')

T = int(input())
for Count in range(T):
    N = int(input())
    List = list(map(int, input().split()))
    Min = abs(List[0])
    count = 0
    for i in range(N):
        if Min > abs(List[i]):
            Min = abs(List[i])
            count = 1
        elif Min == abs(List[i]):
            count += 1
    
    print("#{0} {1} {2}".format(Count+1, Min,count))
