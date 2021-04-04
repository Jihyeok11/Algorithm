import sys
sys.stdin = open("1945in.txt",'r')

def Nanu(N,a):
    b = 0
    if not N%a:
        while not N%a:
            b += 1
            N /= a
        return b
    else:
        return 0



T = int(input())
for Count in range(T):
    N = int(input())
    a = Nanu(N,2)
    b = Nanu(N,3)
    c = Nanu(N,5)
    d = Nanu(N,7)
    e = Nanu(N,11)
    print("#{0} {1} {2} {3} {4} {5}".format(Count+1,a,b,c,d,e))