def route(board, vi, cnt, Min, ay, ax, by, bx):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    if cnt > Min:
        return Min
    if vi[ay][ax] == False:
        return cnt
    vi[ay][ax] = False
    for i in range(4):
        check_ay = ay + dy[i]
        check_ax = ax + dx[i]
        if 0 <= check_ay < len(board) and 0 <= check_ax < len(board[0]):
            if board[check_ay][check_ax] and vi[check_ay][check_ax]:
                r = route(board, vi, cnt + 1, Min, by, bx, check_ay, check_ax)
    return cnt

def solution(board, aloc, bloc):
    answer = 0
    vi = list(list(True for _ in range(len(board[0]))) for _ in range(len(board)))
    answer = route(board, vi, 0, 1000000, aloc[0], aloc[1], bloc[0], bloc[1])


    return answer



print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))