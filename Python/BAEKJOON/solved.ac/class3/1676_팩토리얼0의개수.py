import sys
sys.stdin = open("1676in.txt",'r')

import sys
n = int(sys.stdin.readline())
a = n//125
b = n//25
c = n//5
print(a*3-2*a + 2*b-b+c)