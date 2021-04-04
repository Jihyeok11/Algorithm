import sys
sys.stdin = open("2751in.txt",'r')

import sys
n = int(sys.stdin.readline())
li = sorted( list( int(sys.stdin.readline().strip()) for _ in range(n)))
for i in li:
    print(i)