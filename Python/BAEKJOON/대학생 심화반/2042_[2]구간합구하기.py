import sys
sys.stdin = open("2042in.txt",'r')

import sys

def mySeg(i,left,right):
    global node,li
    if left==right:
        node[i] = li[left]
        return node[i]
    node[i] = mySeg(2*i+1,left,(left+right)//2) + mySeg(2*i+2,(left+right)//2+1,right)
    return node[i]

def myChange(i,idx,diff,left,right):
    if left > idx or right < idx:
        return 0
    node[idx] += diff
    if left != right:
        myChange(i,2*idx+1,diff,left,(left+right)//2)
        myChange(i,2*idx+2,diff,(left+right)//2+1,right)

def mySum(i,start,end,left,right):
    # if start > left or end < right:
    if left > end or right < start:
        return 0
    elif start >= left and end <= right:
        return node[i]
    else:
        return mySum(i*2+1,start,end,left,(left+right)//2) + mySum(i*2+2,start,end,(left+right)//2 +1, right)

n,m,k = map(int,sys.stdin.readline().split()) # m은 숫자 변경, k는 구간 합
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))
node = [0]*100
mySeg(0,0,n-1)
print(node)
for _ in range(m+k):
    a,b,c = map(int,sys.stdin.readline().split())
    if a==1:
        myChange(b-1,0,c-li[b-1],0,n-1)
        print(node)
    else:
        print(mySum(0,b-1,c-1,0,n-1))