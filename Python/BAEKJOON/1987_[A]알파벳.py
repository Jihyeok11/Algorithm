import sys
sys.stdin = open("1987in.txt", "r")


sys.setrecursionlimit(10**5)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
    global answer
    basket = set([(x,y,board[x][y])])

    while basket:
        x, y, ans = basket.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and (board[nx][ny] not in ans):
                basket.add((nx,ny,ans+board[nx][ny]))
                answer = max(answer, len(ans)+1)

R, C = map(int, sys.stdin.readline().split())
board = list(list(x for x in input())for _ in range(R))
answer = 1
bfs(0,0)
print(answer)