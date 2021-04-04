import sys
sys.stdin = open("11659in.txt",'r')

N,M = map(int, input().split())
List = [0]+ list(map(int, input().split()))
for i in range(1,N+1):
    List[i] += List[i-1]

for _ in range(M):
    i,j = map(int, input().split())
    print(List[j]-List[i-1])Zz