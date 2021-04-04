import sys
sys.stdin = open("1258in.txt",'r')

T = int(input())
def box(y,x):
    global LY,LX
    dy = [0,1]
    dx = [1,0] #좌 우 상 하
    for i in range(2):
        C_Y = y + dy[i]
        C_X = x + dx[i]
        if List[C_Y][C_X]:
            if i :
                LY += 1
            else:
                LX += 1
            return box(C_Y,C_X) 

for Count in range(T):
    print("#{0} ".format(Count+1),end='')
    N = int(input())
    List = [list(map(int,input().split())) for _ in range(N)]
    Basket = []
    count = 0
    for Y in range(N):
        for X in range(N):
            if List[Y][X]:
                count += 1
                LY = LX = 1
                box(Y,X)
                for y in range(LY):
                    for x in range(LX):
                        List[Y+y][X+x] = 0
                Basket.append([LY,LX])
    print(count,end=' ')
    Answer = [Basket[0][0],Basket[0][1]]
    if len(Basket)>1:
        for i in range(1,len(Basket)): # Basket 리스트가 한개짜리면 에러가 뜨겟지
            for j in range(len(Answer)//2-1,-1,-1):
                if Answer[0] * Answer[1] > Basket[i][0]*Basket[i][1]:
                    Answer = [Basket[i][0],Basket[i][1]] + Answer
                    break
                elif Basket[i][0]*Basket[i][1] > Answer[2*j]*Answer[2*j+1]:
                    Answer.insert(2*(j+1),Basket[i][1])
                    Answer.insert(2*(j+1),Basket[i][0])
                    break
                elif Basket[i][0]*Basket[i][1] == Answer[2*j]*Answer[2*j+1]:
                    Answer.insert(2*j,Basket[i][1])
                    Answer.insert(2*j,Basket[i][0])
                    break
    print(*Answer)
