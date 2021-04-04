import sys
sys.stdin = open("18111in.txt",'r')

from collections import Counter
n,m,b = map(int,sys.stdin.readline().split())
li = []
for _ in range(n):
    li += list(map(int,sys.stdin.readline().split()))
_sum, _len = sum(li), n * m
li = dict(Counter(li))
ans, minTime = 0,1000000000000000000000

for height in range(257):

    if _len*height <= _sum+b:
        sec = 0
        for key in li:
            if key <= height:
                sec += (height-key)*li[key]
            elif key>height:
                sec += (key-height)*2*li[key]
        if sec <= minTime:
            minTime = sec
            ans = height
print(minTime,ans)