import sys
sys.stdin = open("1931in.txt",'r')

import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    li.append((a,b))
li = sorted(li,key=lambda x:x[0])
li = sorted(li,key=lambda x:x[1])
ed = li[0][1]
ans = 1
for i in range(len(li)):
    if li[i][0] >= ed:
        ed = li[i][1]
        ans += 1
print(ans)