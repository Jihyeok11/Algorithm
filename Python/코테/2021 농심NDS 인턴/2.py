import sys
sys.stdin = open("2in.txt",'r')
dy = [-1,-1,1,1]
dx = [-1,1,-1,1]

            
def solution(bishops):
    answer = 64
    chess = list(list(True for _ in range(8)) for _ in range(8))
    for l in bishops:
        y = ord(l[0]) - 65
        x = int(l[1]) - 1
        answer -= go(y, x, chess, 0)
    return answer

def go(y, x, chess, cnt):
    if chess[y][x]:
        chess[y][x] = False
        cnt += 1
    for i in range(4):
        checkY = y + dy[i]
        checkX = x + dx[i]
        while True:
            if 0<= checkY < 8 and 0 <= checkX < 8:
                if chess[checkY][checkX]:
                    chess[checkY][checkX] = False
                    cnt += 1
                checkY += dy[i]
                checkX += dx[i]
            else:
                break
    return cnt
s = list(input().split())
print(solution(s))