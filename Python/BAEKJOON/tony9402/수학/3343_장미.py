import sys, math
sys.stdin = open("3343in.txt", 'r')

N, A, B, C, D = map(int ,sys.stdin.readline().split())
li = [[A, B], [C, D]]
li = sorted(li, key=lambda x:-x[0])
ans = 10 ** 15
r = math.ceil(N/li[0][0])
for i in range(r, -1, -1):
    res = i *li[0][1]
    res += math.ceil(max(0, N-li[0][0] * i)/li[1][0]) * li[1][1]
    if ans > res:
        ans = res
print(ans)