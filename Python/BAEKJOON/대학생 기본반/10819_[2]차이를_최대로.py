import sys
sys.stdin = open("10819in.txt",'r')

import sys
def orderList(myList):
    if len(myList) == n:
        numbers.append(myList)
        return
    for i in range(n):
        if vi[i]:
            vi[i] = False
            orderList(myList+[i])
            vi[i] = True
def myCount(myList):
    result = 0
    for i in range(n-1):
        result += abs(li[myList[i]] - li[myList[i+1]])
    return result
    
n  = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
numbers = []
vi = [True]*n
orderList([])
Max = 0
for i in numbers:
    res = myCount(i)
    if Max < res:
        Max = res
print(Max)