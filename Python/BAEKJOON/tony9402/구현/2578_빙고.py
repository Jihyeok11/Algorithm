import sys
sys.stdin = open("2578in.txt", 'r')

bingo_board = []
bingo_index = {}
check_bingo_board = list(list(0 for _ in range(5)) for _ in range(5))
check_horizontal = [0, 0, 0, 0, 0]
check_vertical = [0, 0, 0, 0, 0]
check_diagonal = [0, 0]
for y in range(5):
    li = list(map(int, sys.stdin.readline().split()))
    bingo_board.append(li)
    for x in range(5):
        bingo_index[li[x]] = (y,x)
bingo = 0
cnt = 0
for _ in range(5):
    li = list(map(int, sys.stdin.readline().split()))
    for i in range(5):
        cnt += 1
        y, x = bingo_index[li[i]]
        check_bingo_board[y][x] = 1
        v = h = d1 = d2 = 0
        for j in range(5):
            v += check_bingo_board[j][x]
            h += check_bingo_board[y][j]
            d1 += check_bingo_board[j][j]
            d2 += check_bingo_board[4-j][j]
        if v == 5 and not check_vertical[x]:
            bingo += 1
            check_vertical[x] = 1
        if h == 5 and not check_horizontal[y]:
            bingo += 1
            check_horizontal[y] = 1
        if not check_diagonal[0] and d1 == 5:
            bingo += 1
            check_diagonal[0] = 1
        if not check_diagonal[1] and d2 == 5:
            bingo += 1
            check_diagonal[1] = 1
        if bingo >= 3:
            print(cnt)
            exit()