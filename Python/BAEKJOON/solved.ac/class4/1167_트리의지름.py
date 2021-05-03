import sys
from collections import deque
sys.stdin= open("1167in.txt",'r')

def longest(i):
    s = [i]
    vi = [10**10]*(n+1)
    vi[i] = 0
    li = []
    for a in ba[i]:
        li.append(a)
        vi[a[0]] = a[1]
    li.sort()
    while li:
        idx,dist = li.pop(0) # 3,2
        s.append(idx)
        for a in ba[idx]: # (1,2) (4,3)
            if not a[0] in s:
                if dist+a[1] < vi[a[0]]:
                    vi[a[0]] = dist+a[1]
                    li.append((a[0],dist+a[1]))
                    li.sort()
    max_dist = max(vi[1:])
    max_idx = vi.index(max_dist)
    print(max_dist,max_idx)
    print(vi)

    return max_idx,max_dist

ba = {}
n = int(sys.stdin.readline().strip())
for _ in range(n):
    li = list(map(int,sys.stdin.readline().split()))
    ba[li[0]] =[]
    for i in range(1,len(li)-1,2):
        ba[li[0]].append((li[i],li[i+1]))
max_idx,max_dist = longest(1)
print(longest(max_idx)[1])