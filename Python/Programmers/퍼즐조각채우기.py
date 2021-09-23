def nominus(tp):
    minY = minX = 50
    for i in tp:
        minY = min(minY, i[0])
        minX = min(minX, i[1])
    if minY:
        for i in range(len(tp)):
            tp[i][0] -= minY
    if minX:
        for i in range(len(tp)):
            tp[i][1] -= minX
    return tp
    
def solution(game_board, table):
    answer = 0
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    n = len(game_board)
    vi = list(list(True for _ in range(n)) for _ in range(n))
    blocks = []
    for y in range(n):
        for x in range(n):
            if vi[y][x] and table[y][x]:
                ba = [(y, x)]
                tp = [[0, 0]]
                vi[y][x] = False
                while ba:
                    newY, newX = ba.pop(0)
                    for i in range(4):
                        checkY = newY + dy[i]
                        checkX = newX + dx[i]
                        if 0 <= checkY < n and 0<= checkX < n and vi[checkY][checkX] and table[checkY][checkX]:
                            vi[checkY][checkX] = False
                            tp.append([checkY - y, checkX - x])
                            ba.append((checkY, checkX))
                tp = nominus(tp)
                blocks.append(tp)
    print(blocks)
    




    return answer



[
    [[0, 0], [1, 0]], 
    [[0, 0], [0, 1], [1, 1], [2, 1], [2, 2]], 
    [[0, 1], [1, 1], [2, 1], [1, 0]], 
    [[0, 0], [0, 1], [1, 1]], 
    [[0, 0], [0, 1]]
]
# 14
print(solution(	[[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))

print(solution(	[[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]])) # 0
