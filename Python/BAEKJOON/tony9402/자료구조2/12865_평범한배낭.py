import sys
sys.stdin = open("12865in.txt", 'r')

n, k = map(int, sys.stdin.readline().split())
li = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
ba = list(list(0 for _ in range(k+1)) for _ in range(n+1))
for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= li[i-1][0]:
            ba[i][j] = max(ba[i-1][j], ba[i-1][j - li[i-1][0]] + li[i-1][1])
        else:
            ba[i][j] = ba[i-1][j]
            
print(ba[-1][-1])