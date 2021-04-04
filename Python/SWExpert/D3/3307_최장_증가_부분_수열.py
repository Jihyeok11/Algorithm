import sys
sys.stdin = open("3307in.txt",'r')

def Longest(Longest_List,Cnt):
    global Max
    if Cnt == N:
        if Max < len(Longest_List):
            Max = len(Longest_List)
    else:
        for i in range(Cnt,N):
            if Longest_List[len(Longest_List)-1] <= List[i] and Cnt <= i:
                    Longest(Longest_List+[List[i]],i+1)

for Count in range(int(input())):
    N = int(input())
    List = list(map(int,input().split()))
    Longest_List = [0]
    Max = 0
    Longest(Longest_List,0)
    print("#{} {}".format(Count+1,Max-1))