import sys
sys.stdin = open("1700in.txt",'r')

import sys
n,k = map(int,sys.stdin.readline().split())
li = list(int(x) for x in sys.stdin.readline().split())
outlet = []
answer = 0
while len(outlet) < n:
    b = li.pop(0)
    if not b in outlet:
        outlet.append(b)
while li:
    a = li.pop(0)
    if a in outlet:
        pass
    else:
        answer += 1
        maxIdx = loc = 0
        for i in range(len(outlet)):
            if outlet[i] in li:
                idx = li.index(outlet[i])
                if idx > maxIdx:
                    maxIdx = idx
                    loc = i
            else:
                outlet[i] = a
                break
        else:
            outlet[loc] = a
print(answer)