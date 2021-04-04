import sys
sys.stdin = open("10816in.txt",'r')

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
ai = list(map(int,sys.stdin.readline().split()))
vi = [0]*20000000
for i in li:
    vi[i+10000000] += 1
for i in ai:
    print(vi[i+10000000], end=" ")