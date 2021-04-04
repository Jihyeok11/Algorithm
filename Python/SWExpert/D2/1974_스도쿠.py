import sys
sys.stdin = open("1974_스도쿠in.txt","r")

T = int(input())
for Count in range(T):
    List = [ list(map(int,input().split())) for _ in range(9)]
    flag = True
    
    for i in range(9):
        if sum(List[i])==45:
            pass
        else : 
            flag = False
    for i in range(9):
        total = 0
        for j in range(9):
            total += List[j][i]
        if total == 45:
            
            pass
        else :
            flag = False
    
    
    for l in range(3):
        for k in range(3):
            total = 0
            for i in range(3*l,3*(l+1)):
                for j in range(3*k,3*(k+1)):
                    total += List[i][j]
            if total == 45:
                pass
            else :
                flag = False

    
    if flag:
        print("#{0} {1}".format(Count+1,1))
    elif flag != True:
        print("#{0} {1}".format(Count+1,0))