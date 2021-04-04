Dict = {}
def pascal(Y,X):
    key = (Y,X)
    if Y == 1:
        return 1
    if X == 1:
        return 1
    if key in Dict :
        return Dict[key]
    else : 
        Dict[key] = pascal(Y-1,X) + pascal(Y,X-1)
        return Dict[key]%(100000000)

a,b = map(int, input().split())
print(pascal(a,b))