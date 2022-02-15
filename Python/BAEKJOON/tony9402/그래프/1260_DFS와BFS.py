import sys
from collections import defaultdict, deque
sys.stdin = open("1260in.txt", 'r')

def dfs(checks):
    for i in lists[checks]:
        if visited_dfs[i]:
            visited_dfs[i] = False
            dfs_lists.append(i)
            dfs(i)

def bfs(v):
    bfs_basket = deque([v])
    while bfs_basket:
        checks = bfs_basket.popleft()
        for i in lists[checks]:
            if visited_bfs[i]:
                visited_bfs[i] = False
                bfs_basket.append(i)
                bfs_lists.append(i)        

n, m, v = map(int, sys.stdin.readline().split())
lists = defaultdict(list)
bfs_lists = [v]
dfs_lists = [v]
visited_dfs = list(True for _ in range(n+1))
visited_bfs = list(True for _ in range(n+1))
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    lists[a].append(b)
    lists[b].append(a)
for i in range(1, n+1):
    lists[i] = sorted(lists[i], key = lambda x:x)
visited_dfs[v] = False
visited_bfs[v] = False
dfs(v)
print(*dfs_lists)
bfs(v)
print(*bfs_lists)