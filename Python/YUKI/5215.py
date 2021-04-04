import sys
sys.stdin = open("5215in.txt",'r')

def Berrrg(idx,_sum,total):
    global Max
    
    if total > Limit:
        return


    if _sum > Max:
        Max = _sum

    for i in range(N):
        if use_check[i] == True:
            use_check[i] = False
            
            Berrrg(idx+1,_sum + List[i][0], total + List[i][1])
            use_check[i] = True
        

T = int(input())
for Count in range(T):
    print("#{0} ".format(Count+1),end='')
    N , Limit = map(int,input().split())
    use_check = [True] * N
    List = []
    for i in range(N):
        A,B = map(int,input().split())
        List.append((A,B))
    Max = 0
    Berrrg(0,0,0)
    print(Max)
    