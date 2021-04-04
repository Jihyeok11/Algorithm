import sys
sys.stdin = open("1865in.txt",'r')

def permutations(level, product):
    # print(level,'level ->',path,product,visit)
    global maxPercentage
    if level == N:
        # print(path)
        # print(product)
        maxPercentage = max(maxPercentage, product)
 
    for i in range(N):
        if not visit[i] and product * bound[level] > maxPercentage and product * board[level][i] > maxPercentage:
            visit[i] = 1
            path.append(board[level][i])
            permutations(level + 1, product * (board[level][i]))
            path.pop()
            visit[i] = 0
 
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]
    bound = [max(board[x]) for x in range(N)] + [1]
    for i in range(N - 1, -1, -1):
        bound[i] *= bound[i + 1]
 
    visit = [0] * N
    maxPercentage = -1
    path = []
    permutations(0, 1)
    print("#%d %.6f" % (test_case, maxPercentage * 100))