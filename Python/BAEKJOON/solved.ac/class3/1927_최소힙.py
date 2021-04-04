import sys,heapq
sys.stdin = open("1927in.txt",'r')

import sys
n = int(sys.stdin.readline())
li =[]
for _ in range(n):
    m = int(sys.stdin.readline())
    if m:
        heapq.heappush(li, m)
    else:
        try:
            print(heapq.heappop(li))
        except:
            print(0)

    
numbers = int(input())
heap = []

#Max Heap
for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)