import sys
sys.stdin = open("2869in.txt",'r')

import sys
a,b,v = map(int,sys.stdin.readline().split())
if (v-a)/(a-b) == int((v-a)//(a-b)):
    res = (v-a)//(a-b)
else:
    res = int((v-a)//(a-b)) + 1
print(1+res)