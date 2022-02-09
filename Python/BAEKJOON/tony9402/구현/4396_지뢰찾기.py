import sys
sys.stdin = open("4396in.txt", 'r')

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

def mine_check(n):
    bomb = True
    for y in range(n):
        for x in range(n):
            if player_check[y][x] == "x":
                if mine_board[y][x] == ".":
                    cnt = 0
                    for i in range(8):
                        checkY = y + dy[i]
                        checkX = x + dx[i]
                        if 0 <= checkY < n and 0 <= checkX < n and mine_board[checkY][checkX] == "*":
                            cnt += 1
                    check_board[y][x] = str(cnt)
                elif bomb and mine_board[y][x] == "*":
                    bomb = False
                    for i in range(n):
                        for j in range(n):
                            if mine_board[i][j] == "*":
                                check_board[i][j] = '*'
    return check_board

n = int(sys.stdin.readline())
mine_board = list(list(x for x in list(sys.stdin.readline().strip())) for _ in range(n))
check_board = list(list('.' for _ in range(n)) for _ in range(n))
player_check = list(list(x for x in list(sys.stdin.readline().strip())) for _ in range(n))
result = mine_check(n)
for i in result:
    print(''.join(i))