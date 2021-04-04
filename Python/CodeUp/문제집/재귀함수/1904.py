def jaegui(n,m):
    if n<=m:
        if n%2:   
            print(n)
        else:
            if not n==m:
                n = n+1
                print(n)

        jaegui(n+2,m)

a,b = map(int,input().split())
jaegui(a,b)