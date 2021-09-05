import sys, heapq
from collections import defaultdict
sys.stdin = open("이중우선순위큐in.txt", 'r')

def solution(operations):
    answer = []
    vi = defaultdict(bool)
    
    up = []
    down = []
    for i in operations:
        a, b = i.split()
        if a == "I":
            b = int(b)
            vi[b] = True
            heapq.heappush(up, b)
            heapq.heappush(down, -1 * b)
        # D일떄
        else:
            # 최솟값 출력
            if up and b == "-1":
                # while up and not vi[up[0]]:
                #     heapq.heappop(up)
                if up:
                    a = heapq.heappop(up)
                    vi[a] = False
                
            elif down and b == "1":
                # while down and not vi[-1 * down[0]]:
                #     heapq.heappop(down)
                if down:
                    a = heapq.heappop(down)
                    vi[-1 * a] = False
            while down and not vi[-1 * down[0]]:
                    heapq.heappop(down)
            while up and not vi[up[0]]:
                heapq.heappop(up)
    if down:
        answer.append(-1 * down[0])
        answer.append(up[0])
        return answer
    else:
        return [0, 0]

n = int(sys.stdin.readline().strip())
li = list(sys.stdin.readline().strip() for _ in range(n))
print(solution(li))