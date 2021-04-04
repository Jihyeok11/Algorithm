import sys
sys.stdin = open("9019in.txt",'r')

import sys
from collections import deque
for _ in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    ba = deque([(a,"")])
    flag = 1
    vi = [True]*10001
    while flag:
        num,word = ba.popleft()
        for i in range(4):
            if i == 0:
                n = (num*2)%10000
                w = word+"D"
            elif i ==1:
                n = num-1
                w = word+"S"
                if n==(-1):
                    n = 9999
            elif i == 2:
                n = (num%1000)*10+num//1000
                w = word +"L"
            elif i==3:
                n = (num%10)*1000+num//10
                w = word+"R"
            if vi[n]:
                vi[n] = False
                if n==b:
                    print(w)
                    flag = 0
                    break
                else:
                    ba.append((n,w))