import sys
sys.stdin = open("1074in.txt",'r')

def zmaze(m,y,x):
    global result
    if y==a and x == b:
        print(result)
        exit(0)

    if m==1:
        result += 1
        return
    
    if not ( y <= a < y + m and x <= b < x+m):
        result += m*m
        return
    zmaze(m//2, y, x )
    zmaze(m//2, y, x + m//2 )
    zmaze(m//2, y + m//2, x )
    zmaze(m//2, y + m//2, x+ m/2 )


result = 0
n,a,b = map(int,sys.stdin.readline().split())
zmaze(2**n,0,0)