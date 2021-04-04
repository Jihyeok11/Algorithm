import sys
sys.stdin = open("6064in.txt",'r')

import sys
input = sys.stdin.readline
def euc(x, y):
    q = []
    while y:
        q.append(x // y)
        x, y = y, x % y
    q.pop()
    a, b = 0, 1
    for i in q[::-1]:
        a, b = b, a - i*b
    return x, a, b

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    d = x-y
    g, a, b = euc(M, N)
    if d % g:print(-1)
    else:
        k = d // g
        K = x - k*a*M
        print((K-1) % (M//g*N) + 1)