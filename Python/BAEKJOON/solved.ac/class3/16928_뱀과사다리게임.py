import sys
sys.stdin = open("16928in.txt",'r')


from collections import deque
n,m = map(int,sys.stdin.readline().split())
maze = list(i for i in range(0,100))
vi = [0]*100
for _ in range(n+m):
    a,b = map(int,sys.stdin.readline().split())
    maze[a-1] = b-1
basket = deque([0])
while basket:
    point = basket.popleft()
    if point+6>=99:
        print(vi[point]+1)
        break
    for i in range(1,7):
        new = maze[point+i]
        if not vi[new]:
            basket.append(new)
            vi[new]=vi[point]+1

    



# from collections import deque

# n, m=map(int, input().split())
# k=101
# g=[*range(k)]
# dist=[-1]*k

# for i in range(n+m) :
#     x, y=map(int, input().split())
#     g[x]=y

# q=deque()
# dist[1]=0
# q.append(1)
# while q :
#     x=q.popleft()
#     for i in range(1, 7) :
#         y=x+i
#         if(y>100) :
#             continue
#         y=g[y]
#         if(dist[y]==-1 or dist[y]>dist[x]+1) :
#             dist[y]=dist[x]+1
#             q.append(y)

# print(dist[-1])