import sys
sys.stdin = open("11866in.txt",'r')

n,k = map(int,sys.stdin.readline().split())
li = list(range(1,n+1))
print("<",end="")
ba = []
idx = 0
cnt = 1
while li:
    idx %= len(li)
    if cnt == k:
        ba.append(li.pop(idx))
        cnt = 1
    else:
        cnt += 1
        idx += 1
for i in range(len(ba)):
    if i==len(ba)-1:
        print(ba[i],end="")
    else:
        print(ba[i],end=", ")
print(">")