import sys
sys.stdin = open("1227in - 복사본.txt",'r')


T = 10
T = 1

def iswall(a,b):
    if a<1 or a>=N-1 or b<1 or b>=N-1 or List[a][b]:
        return True
    return False

for Count in range(T):
    way = int(input())
    N = 30
    print("#{0} ".format(way),end='')
    List = [[int(x) for x in input()] for _ in range(N)]
    #List를 2차배열로 완성
    Start = List[1][1]
    print(Start)
    Y=X=1
    dy = [0,1,-1,0]
    dx = [1,0,0,1]
    BACK = 0
    while List[Y][X]!=3:
        BACK += 1
        for i in range(4):
            CY = Y+dy[i]
            CX = X+dx[i]
            if iswall(CY,CX)==False:
                Y = CY
                X = CX
                List[Y][X] = i+3 #오른쪽이면 3, 아래면 4, 왼쪽이면 5, 위면 6
                continue

        
        if BACK == 10:
            break
    for _ in range(len(List)):
        print(*List[_])
    print()