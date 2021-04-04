from collections import defaultdict

Dict = {}

def supersum(a,b):
    key = (a,b)
    if key in Dict:
        return Dict[key]

    if a==0:
        Dict[key] = b
        return b
    else:
        total = 0
        for i in range(1,b+1):
            total += supersum(a-1,i)
        Dict[key] = total
        return total

while True:
    a,b = map(int,input().split())
    print(supersum(a,b))
    