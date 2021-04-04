import sys
sys.stdin = open("9461in.txt",'r')

import sys
li = [1,1,1,2,2,3,4,5,7,9]
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n <= len(li):
        print(li[n-1])
    else:
        ch = n-len(li)
        while ch:
            li.append(li[-1]+li[-5])
            ch -= 1
        print(li[-1])