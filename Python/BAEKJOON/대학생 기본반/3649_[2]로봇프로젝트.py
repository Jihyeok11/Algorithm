import sys
sys.stdin = open("3649in.txt",'r')

import sys

while True:
    try:
        leng = int(sys.stdin.readline()) * 10000000
        n= int(sys.stdin.readline())
        li = []
        for _ in range(n):
            li.append(int(sys.stdin.readline()))
        li.sort()
        fro,end = 0,max(0,n-1)
        while True: 
            if fro == end:
                print("danger")
                break
            if li[fro]+li[end]==leng:
                print("yes {} {}".format(li[fro],li[end]))
                break
            elif li[fro]+li[end] > leng:
                end -= 1
            elif li[fro]+li[end] < leng:
                fro += 1
    except:
        break
