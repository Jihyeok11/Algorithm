
# visited를 append 방식으로 사용하니 시간초과
def solution(y,x):
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    st = [(y,x,1)]
    while(st) :
        y, x, cnt = st.pop(0)
        visited[y][x] = True
        block = mat[y][x]

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == False:
                if mat[ny][nx]-1 <= block <= mat[ny][nx]+1:
                    if (ny+1,nx+1) == (n,m) :
                        return cnt+1
                    st.append((ny,nx,cnt+1))
    else :
        return 0


n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

print(solution(0,0))