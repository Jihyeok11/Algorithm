import sys, heapq
sys.stdin = open("13164in.txt", 'r')

n, k = map(int, sys.stdin.readline().split())
li = sorted(list(map(int ,sys.stdin.readline().split())), key= lambda x:x)
gaps = []
ans = 0
for i in range(n - 1):
    heapq.heappush(gaps, li[i+1] - li[i])
for i in range(n - k):
    ans += gaps[i]
gaps.sort()
print(ans)