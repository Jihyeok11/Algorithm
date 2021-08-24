import sys
sys.stdin = open("2212in.txt", 'r')

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
li = sorted(list(map(int, sys.stdin.readline().strip().split())), key = lambda x : x)
res = []
if k>= n:
    print(0)
else:
    for i in range(1, n):
        res.append(li[i] - li[i - 1])
    res.sort()
    for i in range(k-1):
        res.pop()
    print(sum(res))