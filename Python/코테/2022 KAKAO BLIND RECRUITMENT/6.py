def solution(board, skill):
    answer = 0
    for s in skill:
        tp, sy, sx, ey, ex, dm = map(int, s)
        for y in range(sy, ey + 1):
            for x in range(sx, ex + 1):
                if tp == 1:
                    board[y][x] -= dm
                else:
                    board[y][x] += dm
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] > 0:
                answer += 1
    return answer




print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))