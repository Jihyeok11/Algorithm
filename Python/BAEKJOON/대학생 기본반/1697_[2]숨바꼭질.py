import sys
sys.stdin = open("1697in.txt",'r')
import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())
vi = [True]*200000
ba = deque([(n,0)])
while True:
    loc,time = ba.popleft()
    if loc == k:
        print(time)
        break
    if 0<= loc-1 and vi[loc-1]:
        vi[loc-1]=False
        ba.append((loc-1,time+1))
    if loc+1 <= 100000 and vi[loc+1]:
        vi[loc+1]=False
        ba.append((loc+1, time+1))
    if 2*loc <= 100000:
        vi[2*loc] = False
        ba.append((loc*2, time+1))