import sys

import heapq
sys.stdin = open("13975in.txt", 'r')

for _ in range(int(sys.stdin.readline())):
    answer = 0
    n = int(sys.stdin.readline())
    ba = list(map(int, sys.stdin.readline().strip().split()))
    li = []
    for i in range(n):
        heapq.heappush(li, ba[i])
    while len(li) > 1:
        a = heapq.heappop(li)
        b = heapq.heappop(li)
        answer += (a + b)
        heapq.heappush(li, a+b)
    print(answer)