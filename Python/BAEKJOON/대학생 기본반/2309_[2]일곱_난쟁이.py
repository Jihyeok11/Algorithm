import sys
sys.stdin = open("2309in.txt",'r')

import sys
def hund(idx,height,re):
    global res
    if len(re)==7:
        if height==100:
            res.append(re)
        return
    if height >= 100:
        return

    for i in range(idx,9):
        if vi[i]:
            vi[i] = False
            hund(idx+1,height+li[i],re+[li[i]])
            vi[i] = True


li = []
for _ in range(9): 
    li.append(int(sys.stdin.readline()))
vi = [True]*9
res = []
hund(0,0,[])
answer = res[0]
answer.sort()
for i in answer:
    print(i)