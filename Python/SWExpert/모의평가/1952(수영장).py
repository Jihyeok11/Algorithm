import sys
sys.stdin = open("1952in.txt",'r')

def Cost():
    for i in range(1,len(List)):
        if List[i]:
            cost[i] = min(cost[i-1] + Bill1D*List[i] , cost[i-1] + Bill1M,cost[i-3] + Bill3M)
        else:
            cost[i] = cost[i-1]


T = int(input())
for Count in range(T):
    print("#{0} ".format(Count+1), end='')

    Bill1D,Bill1M,Bill3M, Bill1Y = map(int,input().split())
    List = list(map(int,input().split()))
    List = [0]*3 + List
    cost = [0] * len(List)
    Cost()
    if cost[14] > Bill1Y:
        print(Bill1Y)
    else:
        print(cost[14])