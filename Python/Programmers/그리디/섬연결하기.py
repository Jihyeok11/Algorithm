import sys, heapq
from collections import defaultdict
sys.stdin = open("섬연결하기in.txt", 'r')


def solution(n, costs):
    answer = 0
    vi = list(True for _ in range(n))
    town = defaultdict(list)
    for i in costs:
        town[i[0]].append([i[1], i[2]])
        town[i[1]].append([i[0], i[2]])
    # 시작점의 위치를 0
    vi[0] = False
    li = []
    # 0에서 이동할 수 있는 곳을 li에 저장한다. 가장 짧은 길로 가면 되므로 길을 기준으로 heappush해준다.
    for i in town[0]:
        heapq.heappush(li, [i[1], i[0]])
    # 모든 길은 연결 되어 있으므로, 모든 길을 다 돌때까지 실행하면 된다.
    while li:
        length, dest = heapq.heappop(li)
        if vi[dest]:
            vi[dest] = False
            answer += length
            for i in town[dest]:
                heapq.heappush(li, [i[1], i[0]])
    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
