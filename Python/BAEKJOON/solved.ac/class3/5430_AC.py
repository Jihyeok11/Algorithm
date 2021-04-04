import sys
sys.stdin = open("5430in.txt",'r')

import sys
for _ in range(int(sys.stdin.readline())):
    p = sys.stdin.readline().strip()
    p = p.replace('RR','')
    n = int(sys.stdin.readline())
    ac = sys.stdin.readline().strip()[1:-1]
    if ac:
        ac = list(map(int,ac.split(',')))
    else:
        ac = []
    left = True
    for st in p:
        if st == "R":
            left = not left
        elif st == "D":
            try:
                if left:
                    ac.pop(0)
                else:
                    ac.pop()
            except:
                print("error")
                break
    else:
        if left:
            print(str(ac).replace(' ',''))
        else:
            print(str(ac[::-1]).replace(' ',''))