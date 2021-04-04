import sys
sys.stdin = open("1948in.txt",'r')

T = int(input())

Dict = {1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31,
    }

for Count in range(T):
    M1,D1,M2,D2 = map(int,input().split())
    Max_M1 = Dict[M1]
    Max_M2 = Dict[M2]
    total = 0
    for Month in range(M1,M2+1):
        total += Dict[Month]
    print("#{0} {1}".format(Count+1,total-(Max_M2-D2)-D1+1))