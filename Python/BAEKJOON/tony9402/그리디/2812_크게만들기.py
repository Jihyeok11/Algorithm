import sys
sys.stdin = open("2812in.txt", 'r')

n, k = map(int, sys.stdin.readline().strip().split())
li =  list(int(x) for x in sys.stdin.readline().strip())
K, res = k, []
for i in range(n):
    while res and K and res[-1] < li[i]:
        res.pop()
        K -= 1
    res.append(li[i])
print("".join(list(str(x) for x in res[:n-k])))