import sys
sys.stdin = open("in.txt",'r')

M,N = map(int,input().split())
List = [ list(map(int,input().split())) for _ in range(N)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def Tomato():
    global visited,count
    answer = 0
    while (count<N*M) and len(basket):
        answer += 1
        for _ in range(len(basket)):
            Y,X = basket.pop(0)
            for i in range(4):
                newY = Y + dy[i]
                newX = X + dx[i]
                if 0 <= newX < M and 0 <= newY < N and not List[newY][newX] and visited[newY][newX]:
                    visited[newY][newX] = False
                    count += 1
                    basket.append((newY,newX))

    if len(basket):
        return answer
    else:
        return -1

visited = [ [ True for _ in range(M)] for _ in range(N) ] 
basket = []
count = 0
for y in range(N):
    for x in range(M):
        if List[y][x]==1:
            visited[y][x] = False
            count += 1
            basket.append((y,x))
        elif List[y][x] == -1:
            visited[y][x] = False
            count += 1
answer = Tomato()
print(answer)