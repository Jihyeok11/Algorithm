import sys
sys.stdin = open("3314in.txt",'r')

for Count in range(int(input())):
    List = list(map(int,input().split()))
    for i in range(len(List)):
        List[i] = max(40,List[i])
    print("#{} {}".format(Count+1,sum(List)//len(List)))