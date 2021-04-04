import sys
sys.stdin = open("1016in.txt",'r')

import sys
def era(a,b):
    global answer
    for i in range(2,int(b**0.5)+1):
        start = a % (i**2)
        
        for j in range()

a,b = map(int,sys.stdin.readline().split())
li = [True] * (b-a+1)
answer = 0
era(a,b)
print(b-a-answer+1)