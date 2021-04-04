import sys
sys.stdin = open("2609in.txt",'r')

a,b = map(int,sys.stdin.readline().split())
c = min(a,b)
d = a+b-c
e = 1
for i in range(1,c+1):
    if (not c%i) and (not d%i):
        e = i
print(e)
print( e * (c//e) * (d//e))