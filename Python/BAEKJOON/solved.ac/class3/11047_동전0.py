import sys
sys.stdin = open("11047in.txt",'r')

n, k = map(int,sys.stdin.readline().split())
li = sorted(list( int(sys.stdin.readline()) for _ in range(n)), key=lambda x:-x)
ans = 0
for i in li:
    if k//i:
        ans += k//i
        k -= (k//i)*i
    if not k:
        break
print(ans)