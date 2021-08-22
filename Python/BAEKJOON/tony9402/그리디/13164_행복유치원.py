import sys, bisect
sys.stdin = open("13164in.txt", 'r')

n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
gaps = []
ans = 0
for i in range(n - 1):
    # bisect.insort(gaps, li[i+1] - li[i])
    gaps.append(li[i+1] - li[i])
gaps.sort()
for i in range(n - k):
    ans += gaps[i]
print(ans)