import sys
sys.stdin = open("2042in.txt",'r')

import sys
n,m,k = map(int,sys.stdin.readline().split())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))
left = 0
right = n-1
mySum = sum(li)
for _ in range(m+k):
    a,b,c = map(int,sys.stdin.readline().split())
    b-=1
    if a==1:
        mySum -= li[b]
        li[b] = c
        mySum += li[b]
    else:
        c -= 1
        if left < b:
            for i in range(left,b):
                mySum -= li[i]
            left = b
        elif left > b:
            for i in range(b,left):
                mySum += li[i]
            left = b
        
        if c < right:
            for i in range(c+1,right+1):
                mySum -= li[i]
            right = c
        elif c > right:
            for i in range(right+1,c+1):
                mySum += li[i]
            right = c
        print(mySum)