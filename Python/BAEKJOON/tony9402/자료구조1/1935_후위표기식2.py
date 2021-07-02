import sys
from collections import deque
sys.stdin = open("1935in.txt",'r')


n = int(sys.stdin.readline())
li = deque(list(x for x in input().strip()))
numList = []
for _ in range(n):
    numList.append(int(sys.stdin.readline()))
ba = []
while li:
    a = li.popleft()
    if a.isalpha():
        ba.append(numList[ord(a)-65])
    else:
        num1 = ba.pop()
        num2 = ba.pop()
        if a == "+":
            ba.append(num1 + num2)
        elif a == "-":
            ba.append(num2 - num1)
        elif a == "*":
            ba.append(num2 * num1)
        elif a == "/":
            ba.append(num2 / num1)
print(format(ba.pop(), ".2f"))