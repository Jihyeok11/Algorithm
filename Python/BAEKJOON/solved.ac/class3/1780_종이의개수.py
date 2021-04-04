import sys
sys.stdin = open("1780in.txt",'r')

def paper(k,a,b):
    global ba
    s = li[a][b]
    if k==1:
        ba[s]+= 1
        return
    for y in range(k):
        for x in range(k):
            if li[a+y][b+x] != s:
                break
        if li[a+y][b+x] != s:
            break
    else:
        ba[s] += 1
        return
    paper(k//3,a,b)
    paper(k//3,a,b+k//3)
    paper(k//3,a,b+2*(k//3))
    paper(k//3,a+(k//3),b)
    paper(k//3,a+(k//3),b+k//3)
    paper(k//3,a+(k//3),b+2*(k//3))
    paper(k//3,a+2*(k//3),b)
    paper(k//3,a+2*(k//3),b+k//3)
    paper(k//3,a+2*(k//3),b+2*(k//3))

n = int(sys.stdin.readline())
li = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
ba = {-1: 0, 0: 0, 1: 0}
paper(n,0,0)
print(ba[-1])
print(ba[0])
print(ba[1])