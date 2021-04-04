import sys
sys.stdin = open("7568in.txt",'r')

import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    li.append((a,b))
res = [1]*n
for i in range(n):
    for j in range(i+1,n):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            res[i] += 1
        elif li[i][0] > li[j][0] and li[i][1] > li[j][1]:
            res[j] += 1
print(*res)