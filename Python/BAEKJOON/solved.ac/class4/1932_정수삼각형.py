import sys
sys.stdin = open("1932in.txt",'r')

n = int(sys.stdin.readline())
li = list( list(int(x) for x in sys.stdin.readline().split()) for _ in range(n))
# [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            li[i][j] += li[i-1][j]
        elif j==i:
            li[i][j] += li[i-1][j-1]
        else:
            li[i][j] += max(li[i-1][j-1],li[i-1][j])
print(max(li[i]))