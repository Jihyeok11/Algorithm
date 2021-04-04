import sys
sys.stdin = open("Test.txt",'r')

W,H = map(int,input().split())
N = int(input())
List = [[0 for _ in range(H)] for _ in range(W)]
for Count in range(N):
    
    Len, Dir, Y,X = map(int,input().split())
    X -=1
    Y -=1
    if Dir == 0:
        for c in range(Len):
            List[Y][X+c]=1
    elif Dir:
        for c in range(Len):
            List[Y+c][X]=1
for _ in range(len(List)):
    print(*List[_])