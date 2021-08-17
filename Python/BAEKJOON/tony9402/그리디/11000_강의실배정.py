import sys, heapq
sys.stdin = open("11000in.txt" ,'r')

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    a, b = map(int,sys.stdin.readline().strip().split())
    li.append((a, b))
li = sorted(li, key= lambda x : x[0])

room = []
heapq.heappush(room, li[0][1])

for i in range(1, n):
    if li[i][0] < room[0]:
        heapq.heappush(room, li[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, li[i][1])
print(len(room))