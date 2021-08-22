import sys
sys.stdin = open("13164in.txt", 'r')
input = sys.stdin.readline
 
n,k = map(int,input().split())
arr = list(map(int,input().split()))
result = 0
temp = [] 
for i in range(1,n):
    temp.append(arr[i] - arr[i-1])
temp.sort()
 
if k == n:
    result = 0
    print(result)
else:
    for i in range(n-k):
        result += temp[i]
    print(result)
