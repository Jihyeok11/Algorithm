import sys, heapq
sys.stdin = open("디스크컨트롤러in.txt", 'r')

def solution(jobs):
    answer = time = 0
    heap = []
    n = len(jobs)
    jobs.sort()
    vi = list(True for _ in range(n))
    while any(vi) or heap:
        if heap and heap[0][0] > 0:
            heap[0][0] -= 1
            if heap[0][0] == 0:
                a, b = heapq.heappop(heap)
                answer += (time - b)
                print(a, b, ", time : ", time, answer)
        elif heap and not heap[0][0]:
            while not heap[0][0]:
                heapq.heappop(heap)
        for i in range(n):
            if vi[i] and jobs[i][0] <= time:
                vi[i] = False
                heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
        print(time, heap)
        time += 1
    return round(answer // n)

n = int(sys.stdin.readline())
li = list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(n))
print(solution(li))