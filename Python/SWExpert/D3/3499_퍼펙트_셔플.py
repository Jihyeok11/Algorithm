import sys
sys.stdin = open("3499in.txt",'r')

for Count in range(int(input())):
    print("#{} ".format(Count+1),end='')
    Number = int(input())
    Limit = round((Number+0.001)/2)
    Sheet = input().split()
    ASheet = Sheet[:Limit]
    BSheet = Sheet[Limit:]
    for i in range(len(BSheet)):
        ASheet.insert(2*i+1,BSheet[i])
    print(*ASheet)