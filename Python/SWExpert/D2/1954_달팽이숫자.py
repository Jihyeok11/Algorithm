import sys
sys.stdin = open("1954in.txt",'r')

X =Y=0
def iswall(a,b):
    if a<0 or a>=N or b<0 or b>=N or List[a][b]!=0 :
        return True
    return False

def direction(a):
    global X,Y
    if a == 0:
        X += 1

    elif a == 1:
        Y += 1

    elif a ==2:
        X -= 1
    elif a ==3:
        Y -= 1

T = int(input())
for Count in range(T):
    
    print("#{0} ".format(Count+1))
    N = int(input())
    
    List = [[0 for _ in range(N)] for _ in range(N)]
    count = 1
    a = 0
    Y = X= 0
    List[0][0] = count
    for c in range(N*N-1):
        count += 1
        direction(a)
        if iswall(Y,X) == False:
            List[Y][X] = count
        elif iswall(Y,X) == True:
            if a == 0:
                X -= 1
            elif a == 1:
                Y -= 1
            elif a == 2:
                X += 1
            elif a ==3:
                Y += 1
            a  = (a+1)%4
            direction(a)
            List[Y][X] = count

    for _ in range(len(List)):
        print(*List[_])

    








































# def check(y, x):
#     return y > -1 and y < size and x > -1 and x < size and arr[y][x] == 0

# def move(y, x):
#     if direction == 1:
#         x += 1
#     elif direction == 2:
#         y += 1
#     elif direction == 3:
#         x -= 1
#     elif direction == 4:
#         y -= 1
#     if check(y, x) == True:
#         return [y,x,direction]
#     else: # 배열 범위 밖일 때, 배열 안에 숫자가 0 이상일 때
#         if direction == 1:
#             return [y+1, x-1, direction+1]
#         elif direction == 2:
#             return [y-1, x-1, direction+1]
#         elif direction == 3:
#             return [y-1, x+1, direction+1]
#         elif direction == 4:
#             return [y+1, x+1, 1]

# T = int(input())
# for Count in range(T):
#     size = int(input())
#     arr = [[0] * size for i in range(size)]

#     order = 1
#     y, x = 0, 0
#     direction = 1 # 1->오른쪽, 2->아래, 3->왼쪽,4-> 위

#     arr[y][x] = order

#     while order < size * size:

#         y, x, direction = move(y, x)
        
#         order += 1
#         arr[y][x] = order
        
#     for i in range(size):
#         for j in range(size):
#             print(arr[i][j], end= ' ')
#         print()
