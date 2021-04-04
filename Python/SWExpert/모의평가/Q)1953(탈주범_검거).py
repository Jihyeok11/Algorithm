import sys
sys.stdin = open("1953in.txt",'r')

def up(Start,End):
    if Start==1 or Start==2 or Start==4 or Start==7:
        if End == 1 or End == 2 or End == 5 or End == 6:
            return True
        return False

def down(Start, End):
    if Start == 1 or Start == 2 or Start == 5 or Start == 6:
        if End == 1 or End == 2 or End == 4 or End == 7:
            return True
        return False

def left(Start, End):
    if Start == 1 or Start == 3 or Start == 6 or Start == 7:
        if End == 1 or End == 3 or End == 5 or End == 4:
            return True
        return False

def right(Start, End):
    if Start == 1 or Start == 3 or Start == 4 or Start == 5:
        if End == 1 or End == 3 or End == 6 or End == 7:
            return True
        return False

T = int(input())
for Count in range(T):
    N, M, R, C, L = map(int,input().split())
    List = [ list(map(int,input().split())) for _ in range(N)]
    Cnt = 1
    Set = set([(R,C)])
    Queue = [(R,C,Cnt)]
    dy = [0,0,-1,1]
    dx = [1,-1,0,0] #우,좌,상,하

    while Queue:
        Y,X, Cnt = Queue.pop(0)
        if Cnt ==L:
            break
        for i in range(4):
            C_Y = Y + dy[i]
            C_X = X + dx[i]
            if (0<= C_Y < N) and (0 <= C_X < M) and (i==0) and ( right(List[Y][X], List[C_Y][C_X])) == True:
                Queue.append((C_Y,C_X,Cnt+1))
                Set = Set | set([(C_Y,C_X)])
            elif (0<= C_Y < N) and (0 <= C_X < M) and (i==1) and ( left(List[Y][X], List[C_Y][C_X])) == True:
                Queue.append((C_Y,C_X,Cnt+1))
                Set = Set | set([(C_Y,C_X)])
            elif (0<= C_Y < N) and (0 <= C_X < M) and (i==2) and ( up(List[Y][X], List[C_Y][C_X] )) == True:
                Queue.append((C_Y,C_X,Cnt+1))
                Set = Set | set([(C_Y,C_X)])
            elif (0<= C_Y < N) and (0 <= C_X < M) and (i==3) and ( down(List[Y][X], List[C_Y][C_X])) == True:
                Queue.append((C_Y,C_X,Cnt+1))
                Set = Set | set([(C_Y,C_X)])
    print("#{0} {1}".format(Count+1,len(Set)))