import sys, heapq
from collections import defaultdict
sys.stdin = open("섬연결하기in.txt", 'r')


def solution(n, costs):
    vi = list(True for _ in range(n))
    town = defaultdict(list)
    for i in costs:
        town[i[0]].append([i[1], i[2]])
        town[i[1]].append([i[0], i[2]])
    s = 0
    li = []
    for i in town[0]:
        heapq.heappush(li, i)
    
    answer = 0
    return answer


n = int(sys.stdin.readline())
li = sys.stdin.readline().strip()
li = li.replace("],[", "/")
li = li.replace(",", "")
li = li.replace("[", "")
li = li.replace("]", "")
tp = li.split("/")
li = []
for i in range(n):
    li.append(list(int(x) for x in tp[i]))

print(solution(n, li))
