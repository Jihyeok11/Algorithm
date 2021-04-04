import sys
sys.stdin = open("Test.txt",'r')

def go(Y,X):
    if List[Y][X+1]==0 or List[Y][X+1]==2:
        X = X+1
        return Y,X
    elif List[Y][X+1]:
        Y = Y+1
        return Y,X

List = [ list(map(int,input().split())) for _ in range(10)]
Y=X=1

while List[Y][X] !=2:
    List[Y][X]=9
    Y,X = go(Y,X)
    if X==Y==8:
        break
List[Y][X] = 9
for _ in range(10):
    print(*List[_])