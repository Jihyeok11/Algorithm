def dfs(idx, _sum):
    global Total
    if idx == N:
        if Total > _sum:
            Total = _sum
        return
        
    if _sum > Total:
        return
    for i in range(N):
        if use_check[i]:
            use_check[i] = False
            dfs(idx+1, _sum + List[idx][i])
            use_check[i] = True

T = int(input())
for Count in range(T):
    print("#{0} ".format(Count+1),end='')
    N = int(input())
    List = [list(map(int,input().split())) for _ in range(N)]
    
    Total = 987654321
    

    use_check = [ True for _ in range(N)]
    
    dfs(0, 0)
    print(Total)