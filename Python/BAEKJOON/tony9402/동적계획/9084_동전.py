import sys
sys.stdin = open("9084in.txt", 'r')

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a, b = map(int, sys.stdin.readline().strip().split())
    money = int(sys.stdin.readline())
    print(n, a, b, money)
    