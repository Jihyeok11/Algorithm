import sys
sys.stdin = open("1097in.txt",'r')

List = [ list(map(int,input().split())) for _ in range(19)]
N = int(input())
for Count in range(N):
    A , B = map(int, input().split())
    A -= 1
    B -= 1
    for i in range(19):
        if not List[A][i]:
            List[A][i]=1
        elif List[A][i]:
            List[A][i] = 0
        if List[i][B]:
            List[i][B] = 0
        elif not List[i][B]:
            List[i][B]=1
        
for i in range(19):
    print(*List[i])
print()