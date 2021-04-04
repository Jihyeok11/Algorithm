import sys
sys.stdin = open("10250in.txt",'r')

n = int(sys.stdin.readline())
for _ in range(n):
    h,w,n = map(int,sys.stdin.readline().split())
    f = n%h
    if not f:
        f = h
    ho = n//h
    if n/h == ho:
        ho -=1
    ho += 1
    if ho>=10:
        print(str(f)+str(ho))
    else:
        print(str(f)+"0"+str(ho))