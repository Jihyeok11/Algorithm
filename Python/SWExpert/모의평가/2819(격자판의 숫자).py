import sys
sys.stdin = open("2819in.txt",'r')

def iswall(Y,X):
    if Y<0 or X<0 or Y>=4 or X>= 4:
        return True
    return False


def Miro(Y,X):
    global Answer, Answer_List
    if len(Answer) == 7:
        if not Answer in Answer_List:
            Answer_List.append(Answer)

    else:
        dy = [0,0,1,-1]
        dx = [-1,1,0,0]
        for i in range(4):
            C_Y = Y + dy[i]
            C_X = X + dx[i]
            if iswall(C_Y, C_X) == False:
                Answer += str(List[C_Y][C_X])
                Miro(C_Y,C_X)
                Answer = Answer[:-1]



T = int(input())
for Count in range(T):
    print("#{0} ".format(Count+1), end = '')
    List = [ list(map(int,input().split())) for _ in range(4) ]
    Answer_List = []
    for Y in range(4):
        for X in range(4):
            Answer = str(List[Y][X])
            Miro(Y,X)
    print(len(Answer_List))