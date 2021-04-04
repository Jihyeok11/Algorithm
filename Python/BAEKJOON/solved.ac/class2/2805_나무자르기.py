import sys
sys.stdin = open("2805in.txt",'r')

import sys
n,m = map(int,sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))
left = 0
right = max(li)
while right >= left:
    mid = (left+right)//2
    res = 0
    for i in li:
        res += max(0,i-mid)
    if res >= m:
        left = mid + 1
    elif res < m:
        right = mid - 1
print(right)
