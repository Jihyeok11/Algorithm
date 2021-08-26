import sys
sys.stdin = open("2812in.txt", 'r')

n, k = map(int, sys.stdin.readline().strip().split())
li =  list(int(x) for x in sys.stdin.readline().strip())
res = []
for i in range(n):
    for j in res:
        if li[i] > res[j]:
            res.pop(j)
            k -= 1
    else:
        res.append(li[i])
print(res)