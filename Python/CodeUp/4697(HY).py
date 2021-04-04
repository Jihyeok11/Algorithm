import copy

N = int(input()) # 배열의 가로/세로 길이
spots = [list(map(int, input().split())) for _ in range(N)] # 높이의 배열
rain = [] # 강수량
answer = [] # 안전영역의 개수
for i in range(N):
    for j in range(N):
        if spots[i][j] not in rain: # rain에 강수량 append
            rain.append(spots[i][j])

for raining in rain: # 강수량의 경우에 따라 for문
    same_spots = copy.deepcopy(spots) # 강수량이 바뀔 때마다 원본 리스트로 초기화
    for i in range(N):
        for j in range(N):
            if same_spots[i][j] <= raining: # 강수량보다 높이가 낮으면
                same_spots[i][j] = 0 # arr[i][j]는 물에 잠김

    # 물에 잠겨진 배열(== same_spots)이 만들어지면 인접한 네방향을 탐색
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    move = []
    cnt_list = []
    for y in range(N):
        for x in range(N):
            cnt = 0 # 이동 횟수 카운트; 이동 횟수까지는 필요하지 않지만 cnt_list의 개수가 안전영역의 개수이므로 사용
            if same_spots[y][x] != 0: # 물에 잠기지 않았으면
                move.append((y,x)) # move에 위치 append
                same_spots[y][x] = 0 # 중복 체크 방지 위해 0으로 초기화
                cnt += 1

                while move: # move에 위치가 있는 동안
                    y, x = move.pop()

                    for f in range(4): # 인접한 네 방향에 안전영역이 또 있는지 확인
                        newY = y + dy[f]
                        newX = x + dx[f]

                        if 0 <= newY and newY < N and 0 <= newX and newX < N: # list index 확인
                            if same_spots[newY][newX] != 0: # 물에 잠기지 않았으면
                                move.append((newY, newX)) # move에 위치 append
                                same_spots[newY][newX] = 0 # 중복 탐색 막기 위해 0으로 초기화
                                cnt += 1 # 이동 횟수 증가
                cnt_list.append(cnt) # cnt_list에 이동 횟수 추가
    answer.append(len(cnt_list)) # 모든 안전영역의 개수 answer에 추가 

print(max(answer)) # answer에 담긴 안전영역의 개수 중에서 최대 개수 출력