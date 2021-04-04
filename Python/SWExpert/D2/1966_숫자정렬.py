import sys
sys.stdin = open("1966in.txt",'r')

T = int(input())

for Count in range(T):
    N = int(input())
    List = list(map(int, input().split()))
    Answer = []
    for i in range(N):
        Min = min(List)
        Answer.append(List.pop(List.index(Min)))
    print("#{0} ".format(Count+1),end='')
    print(*Answer)