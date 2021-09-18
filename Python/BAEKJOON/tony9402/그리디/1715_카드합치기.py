import sys, heapq
sys.stdin = open("1715in.txt", 'r')

n = int(sys.stdin.readline())
ba = []
answer = 0
for _ in range(n):
    heapq.heappush(ba, int(sys.stdin.readline()))

while len(ba) > 1:
    a = heapq.heappop(ba)
    b = heapq.heappop(ba)
    answer += (a + b)
    heapq.heappush(ba, a+b)
print(answer)
    