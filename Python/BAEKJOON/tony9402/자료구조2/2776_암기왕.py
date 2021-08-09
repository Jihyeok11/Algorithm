import sys
sys.stdin = open("2776in.txt", 'r')
from collections import defaultdict
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ask = defaultdict(int)
    for i in list(map(int, sys.stdin.readline().strip().split())):
        ask[i] = 1
    m = int(sys.stdin.readline())
    for i in list(map(int, sys.stdin.readline().strip().split())):
        if ask[i]:
            print(1)
        else:
            print(0)