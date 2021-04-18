import sys
sys.stdin = open("1932in.txt",'r')

n = int(sys.stdin.readline())
li = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
for y in range(1, n):
    for x in range(y+1):
        if x==0:
            li[y][x] += li[y-1][x]
        elif x==len(li[y])-1:
            li[y][x] += li[y-1][x-1]
        else:
            li[y][x] += max(li[y-1][x-1],li[y-1][x])
print(max(li[n-1]))