import sys
sys.stdin = open("in.txt",'r')

n,m = map(int,input().split())
List = [list(map(int,input().split())) for _ in range(n)]
def solution(y,x):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    visited = [[True for _ in range(m)] for _ in range(n)]
    basket = [(0,0,1)] # 방문한 적이 없으면 basket에 append 시킨다.
    while basket:
        for _ in range(len(basket)):
            y,x,cnt = basket.pop(0)
            for i in range(4):
                Y = y+dy[i]
                X = x+dx[i]
                if 0<=Y<n and 0<=X<m and visited[Y][X] and abs(List[y][x]-List[Y][X])<=1:
                    if Y==n-1 and X==m-1:
                        return cnt+1
                    basket.append((Y,X,cnt+1))
                    visited[Y][X] = False
        
    if not basket: # basket에 담긴게    없으면 답은 0
        return 0
print(solution(0,0))

