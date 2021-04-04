import sys
sys.stdin = open("1654in.txt",'r')

import sys
k,n = map(int,sys.stdin.readline().split())
li = []
for _ in range(k):
    li.append(int(sys.stdin.readline()))
left ,right = 1,2**31
while left <= right:
    mid = (left+right)//2
    res = 0
    for i in li:
        res += (i // mid)
    if res >= n:
        left = mid + 1
    elif res <= n:
        right = mid-1
print(left,right)