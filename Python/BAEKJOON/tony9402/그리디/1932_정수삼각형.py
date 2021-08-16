import sys
sys.stdin = open("1932in.txt", 'r')

n = int(sys.stdin.readline())
li = list(list(map(int,sys.stdin.readline().strip().split())) for _ in range(n))
for i in range(1, n):
    for j in range(len(li[i])):
        if j == 0:
            li[i][j] += li[i-1][j]
        elif j == len(li[i]) - 1:
            li[i][j] += li[i-1][j-1]
        else:
            li[i][j] += max(li[i-1][j-1], li[i-1][j])
print(max(li[-1]))