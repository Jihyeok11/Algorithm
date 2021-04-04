import sys
sys.stdin = open("6057in.txt",'r')


def triangle(root, cnt, v):
    global ans
 
    if cnt == 2:
        if root in G[v]:
            ans += 1
        return
    else:
        for w in G[v]:
            if v < w:
                triangle(root, cnt + 1, w)
 
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    ans = 0
 
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
 
    for i in range(1, N + 1):
        triangle(i, 0, i)
 
    print('#{} {}'.format(tc, ans))