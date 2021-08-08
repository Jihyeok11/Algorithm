import sys
from collections import deque, defaultdict
import bisect

sys.stdin = open("7662in.txt",'r')
input = sys.stdin.readline

def solve():
    k = int(input())
    queue = deque()
    cnt = defaultdict(int)
    for _ in range(k):
        flag, num = input().split()
        num = int(num)
        if flag == "I":
            if cnt[num] == 0:
                bisect.insort(queue, num)
                cnt[num] = 1
            else:
                cnt[num] += 1
        elif flag == "D" and num == 1 and queue:
            if cnt[queue[-1]] > 1:
                cnt[queue[-1]] -= 1
            else:
                cnt[queue[-1]] = 0
                queue.pop()
        elif flag == "D" and num == -1 and queue:
            if cnt[queue[0]] > 1:
                cnt[queue[0]] -= 1
            else:
                cnt[queue[0]] = 0
                queue.popleft()
    if queue:
        print(queue[-1], queue[0], sep="\n")
    else:
        print("EMPTY")
        
for _ in range(int(input())):
    solve()