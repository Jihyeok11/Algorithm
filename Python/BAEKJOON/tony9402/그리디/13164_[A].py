import sys, heapq
sys.stdin = open("13164in.txt", 'r')
input = sys.stdin.readline
    
n,k = map(int,input().split())
arr = list(map(int,input().split()))
temp = [] 
result = 0
for i in range(n - 1):
    heapq.heappush(temp, arr[i+1] - arr[i])
    # temp.append(arr[i + 1] - arr[i])
for i in range(n-k):
    result += temp[i]
print(result)
