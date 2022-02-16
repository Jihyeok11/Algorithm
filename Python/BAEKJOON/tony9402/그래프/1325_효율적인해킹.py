import sys
from collections import defaultdict
sys.stdin = open("1325in.txt", 'r')

def stair(a, basket):
    if vi[a]:
        for i in lists[a]:
            if not i in basket:
                cnt[a] += stair(i, basket+[i])
            else:
                vi[a] = True
        vi[a] = False
    return cnt[a]

n, m = map(int, sys.stdin.readline().split())
lists = defaultdict(list)
cnt = list(1 for _ in range(n+1))
vi = list(True for _ in range(n+1))
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    lists[b].append(a)
for i in range(1, n+1):
    if vi[i]:
        stair(i, [i])
answer = []
max_num = 0
for i in range(n+1):
    if max_num < cnt[i]:
        answer = [i]
        max_num = cnt[i]
    elif max_num == cnt[i]:
        answer.append(i)
print(*answer)
print(cnt)