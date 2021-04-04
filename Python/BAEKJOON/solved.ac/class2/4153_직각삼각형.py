import sys
sys.stdin = open("4153in.txt",'r')

import sys
while True:
    li = sorted(list(map(int,sys.stdin.readline().split())))
    if (li[0] == li[1] == li[2]) and (li[0] == 0):
        break
    if (li[2])**2 == (li[1]**2) + (li[0]**2):
        print("right")
    else:
        print("wrong")