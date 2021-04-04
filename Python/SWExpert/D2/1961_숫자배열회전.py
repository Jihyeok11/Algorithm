import sys
sys.stdin = open("1961in.txt",'r')


def clockwise(List):
    N = len(List)
    List_before = List[:]
    List_Answer = [[0 for _ in range(N)] for _ in range(N)]
    for Y in range(N):
        for X in range(N):
            List_Answer[Y][X] = List_before[N-1-X][Y]
    return List_Answer

T = int(input())

for Count in range(T):
    print("#{0}".format(Count+1))
    N = int(input())
    List = [list(map(int, input().split())) for _ in range(N)]
    ListA = clockwise(List)
    ListB = clockwise(clockwise(List))
    ListC = clockwise(clockwise(clockwise(List)))
    
    for i in range(N):
        Str = ''
        for j in range(N):
            Str += str(ListA[i][j])
        Str += ' '
        for j in range(N):
            Str += str(ListB[i][j])
        Str += ' '
        for j in range(N):
            Str += str(ListC[i][j])
        print(Str)