import sys
sys.stdin = open("11399in.txt",'r')

import sys
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
li.sort()
ans = cnt = 0
for i in li:
    ans += (i+cnt)
    cnt += i
print(ans)