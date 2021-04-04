import sys
sys.stdin = open("1949in.txt",'r')




def count(Y,X):
    global cnt
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]


    for i in range(4):
        C_Y = Y + dy[i]
        C_X = X + dx[i]
        if 0<= C_Y < N and 0 <= C_X < N: #벽
            if List[C_Y][C_X] < List[Y][X]:
                cnt += 1
                cnt = last
                last = max(cnt,last)




T = int(input())
for Count in range(T):
    N, K = map(int,input().split())
    List = [ list(map(int,input().split())) for _ in range(N)]
    Mountain = List[:]
    Max = 0
    Mountain_List = []
    cnt = 0
    for Y in range(N):
        for X in range(N):
            if List[Y][X] > Max:
                Mountain_List = [(Y,X)]
                Max = List[Y][X]
            elif List[Y][X] == Max:
                Mountain_List.append((Y,X)) # 최대 지점들의 인덱스들 구함
    
    for i in range(len(Mountain_List)):
        count(Mountain_List[i][0], Mountain_List[i][1])
        print(cnt)
