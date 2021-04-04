def solution(n, horizontal):
    dy = [1,1,-1,0] # 왼쪽 아래로,아래로, 오른쪽 위로, 오른쪽으로
    dx = [-1,0,1,1] # 오른쪽 시작이면 인덱스 0부터, 아래 시작이면 인덱스 2부터
    dt = [2,1,2,1]
    answer = [list(0 for _ in range(n)) for _ in range(n)]
    time = 0
    cnt = 1 # 아예 처음 안움직이게
    # while cnt < n*n+1:
    if horizontal :
        y = 0
        x = 1
        time += 1
        answer[y][x] = time
        engine = 0

    else:
        y = 1
        x = 0
        time += 1
        answer[y][x] = time
        engine = 2


    ny = y+dy[engine]
    nx = x+dx[engine]
    while True:
        while 0<=ny<n and 0<= nx <n:
            cnt += 1
            time += dt[engine]
            answer[ny][nx] = time
            y = ny
            x = nx
            ny = y+dy[engine]
            nx = x+dx[engine]
        engine += 1
        engine %= 4
        if engine%2:
            ny = y+dy[engine]
            nx = x+dx[engine]
            time += dt[engine]
            answer[ny][nx] = time
            y = ny
            x = nx

            engine += 1
            engine %= 4
        ny = y+dy[engine]
        nx = x+dx[engine]

        
    return answer




result = [[0,1,8,9],[3,6,11,20],[4,13,18,21],[15,16,23,24]]
horizontal = True
n = 4
print(solution(n,horizontal))