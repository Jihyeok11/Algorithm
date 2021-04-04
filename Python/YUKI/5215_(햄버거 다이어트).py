import sys
sys.stdin = open("5215in.txt",'r')

def Berrrg(idx,_sum,Cal):
    global Max
    
    if idx != N:
        if not use_check[idx]:
            use_check[idx] = True
            Berrrg(idx+1,_sum,Cal)
            use_check[idx] = False
            Berrrg(idx+1,_sum,Cal)
    if idx == N:
        # use_check[i] 모든 부분집합
        Cal = 0
        total = 0
        for i in range(N):
            if use_check[i]: #True일 때
                Cal += List[i][1]
                total += List[i][0]
                if Cal > Limit:
                    break
            if total > Max:
                Max = total

                

T = int(input())
for Count in range(T):
    print("#{0} ".format(Count+1),end='')
    N , Limit = map(int,input().split())
    use_check = [False] * N
    List = []
    for i in range(N):
        A,B = map(int,input().split())
        List.append((A,B))
    Max = 0
    Berrrg(0,0,0)
    print(Max)
    