import sys
sys.stdin = open("IN.txt",'r')
n,m,count = map(int, input().split())
List = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(count):
    Y1,X1,Y2,X2,u = map(int, input().split())
    List[Y1][X1] = List[Y1][X1]+u
    if Y2+1<n and X2+1<m:
        List[Y2+1][X2+1] = List[Y2+1][X2+1]+u
    if X2+1<m:
        List[Y1][X2+1] = List[Y1][X2+1]-u
    if Y2+1<n :
        List[Y2+1][X1] = List[Y2+1][X1]-u
for _ in range(len(List)):
    print(*List[_])
print()
for Y in range(1,n):
    for X in range(1,m):
        List[Y][X] += List[Y-1][X]+List[Y][X-1]-List[Y-1][X-1]
for _ in range(len(List)):
    print(*List[_])