import sys
sys.stdin = open("1074in.txt", 'r')

def myZ(m, y, x):
    global answer
    if y == r and x == c:
        print(answer)
        exit()

    if m == 1:
        answer += 1
        return
    
    if not (y <= r < y + m and x <= c < x + m):
        answer += m**2
        return

    myZ(m//2, y, x)
    myZ(m//2, y, x + m//2)
    myZ(m//2, y + m//2, x)
    myZ(m//2, y + m//2, x + m//2)
    

answer = 0
N, r, c = map(int ,sys.stdin.readline().split())
myZ(2**N, 0, 0)