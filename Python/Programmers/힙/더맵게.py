import sys
import heapq
sys.stdin = open("더맵게in.txt", 'r')

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    while heap[0] < K:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a + 2 * b)
        answer += 1

    return answer

li = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())
print(solution(li, k))