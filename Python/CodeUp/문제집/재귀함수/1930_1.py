Dict = {}
def supersum(a,b):
    
    key = (a,b)
    
    if not a:
        Dict[key] = b
        return b

    elif key in Dict:
        return Dict[key]

    else:
        total = 0
        for i in range(1,b+1):
            total += supersum(a-1,i)
        Dict[key] = total
        return Dict[key]
    print()

while True:
    a,b = map(int,input().split())
    print(supersum(a,b))

