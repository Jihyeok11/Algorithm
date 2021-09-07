import sys, heapq
sys.stdin = open("디스크컨트롤러in.txt", 'r')

def solution(jobs):
    n = len(jobs)
    answer = 0
    heap = []
    jobs = sorted(jobs, key = lambda x : (x[0], x[1]))
    a,b = jobs.pop(0)
    heap.append([b, a])
    time = a
    while jobs or heap:
        while jobs and jobs[0][0] <= time:
            a, b = jobs.pop(0)
            heapq.heappush(heap, [b, a])
        if heap:
            c, d = heapq.heappop(heap)
            # 잔량, 초기시간
            time += c
            answer += (time - d)
            print(answer)
        else:
            a, b = jobs.pop(0)
            heapq.heappush(heap, [b, a])
            time = a
    return round(answer // n)

n = int(sys.stdin.readline())
li = list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(n))
print(solution(li))