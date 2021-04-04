import sys
sys.stdin = open("11651in.txt",'r')

import sys
n = int(sys.stdin.readline())
for i in sorted( list( list(map(int,sys.stdin.readline().split())) for _ in range(n)), key = lambda x:(x[1],x[0])):
    print("{} {}".format(i[0],i[1]))