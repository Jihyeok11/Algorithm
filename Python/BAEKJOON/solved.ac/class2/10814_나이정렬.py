import sys
sys.stdin = open("10814in.txt",'r')

import sys
n = int(sys.stdin.readline())
li = sorted(list(list(sys.stdin.readline().split() +[i]) for i in range(n)), key=lambda x :(int(x[0]),x[2]))
for i in li:
    print("{} {}".format(i[0],i[1]))