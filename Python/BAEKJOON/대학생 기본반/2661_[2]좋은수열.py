import sys
sys.stdin = open("2661in.txt",'r')

import sys

def sequence(word):
    for i in range(1,len(word)//2+1):
        if word[-i:] == word[-2*i:-i]:
            return

    if len(word)==n:
        print(word)
        return True
    
    for i in range(1,4):
        if sequence(word+str(i)):
            return True

n = int(sys.stdin.readline())
ans = "1"
sequence(ans)