import sys
sys.stdin = open("5431in.txt",'r')

T =int(input())
for Count in range(T):
    N, K = map(int,input().split())
    Answer_List = [x+1 for x in range(N)]
    List = []
    for i in map(int,input().split()):
        List.append(i)
    List.sort()
    while List:
        Answer_List.pop(List.pop()-1)
    print("#{} ".format(Count+1),end="")
    print(*Answer_List)