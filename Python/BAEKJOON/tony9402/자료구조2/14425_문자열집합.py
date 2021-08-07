import sys
sys.stdin = open("14425in.txt",'r')

n, m = map(int,sys.stdin.readline().strip().split())
ba = {}
ans = 0 
for _ in range(n):
    ba[sys.stdin.readline().strip()] = True
for _ in range(m):
    if sys.stdin.readline().strip() in ba:
        ans += 1
print(ans)