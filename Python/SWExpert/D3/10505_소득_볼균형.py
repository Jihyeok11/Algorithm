import sys
sys.stdin = open("10505in.txt",'r')

for Count in range(int(input())):
    N = int(input())
    List = list(map(int,input().split()))
    answer = 0
    for i in range(N):
        if List[i]<=(sum(List)/N):
            answer += 1
    print("#{} {}".format(Count+1,answer))