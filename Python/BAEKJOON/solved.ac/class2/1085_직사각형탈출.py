import sys
sys.stdin = open("1085in.txt",'r')

import sys
x,y,w,h = map(int,sys.stdin.readline().split())
print(min(y,x,abs(h-y),abs(w-x)))