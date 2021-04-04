import sys
sys.stdin = open("2630in.txt",'r')


def sq(n,a,b):
    global ba
    s = li[a][b]
    for y in range(n):
        for x in range(n):
            if li[a+y][b+x] != s:
                break
        if li[a+y][b+x] != s:
            break
    else:
        ba[s] += 1
        return
    sq(n//2,a,b)
    sq(n//2,a,b+n//2)
    sq(n//2,a+n//2,b)
    sq(n//2,a+n//2,b+n//2)
            

n = int(sys.stdin.readline())
li = list( list( map(int,sys.stdin.readline().split())) for _ in range(n))
ba = {0:0, 1:0}
sq(n,0,0)
print(ba[0])
print(ba[1])