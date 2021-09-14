from collections import defaultdict
def solution(info, edges):
    answer = 0
    routes = defaultdict(list)
    for i in edges:
        routes[i[0]].append(i[1])
    vi = list(True for _ in range(len(info)))
    vi[0] = False
    # 양, 총 양
    li = [(0, 1)]
    while li:


    return answer



print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))