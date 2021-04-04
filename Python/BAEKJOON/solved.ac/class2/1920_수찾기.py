import sys
sys.stdin = open("1920in.txt",'r')

n = int(sys.stdin.readline())
li = set(list(map(int,sys.stdin.readline().split())))
m = int(sys.stdin.readline())
ba = list(map(int,sys.stdin.readline().split()))
for i in ba:
    if li&set([i]):
        print(1)
    else:
        print(0)