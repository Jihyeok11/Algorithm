import sys
sys.stdin = open("19598in.txt", 'r')

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    li.append((a, 1))
    li.append((b, -1))
# li = sorted(li, key = lambda x : (x[0]. x[1]))
li.sort()
r = 0
ans = 0
for _, a in li:
    r += a
    ans = max(ans, r)
print(ans)