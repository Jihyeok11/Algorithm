import sys
sys.stdin = open("1966in.txt", 'r')

for _ in range(int(sys.stdin.readline())):
    n, m = map(int,sys.stdin.readline().split())
    ba = list(map(int, sys.stdin.readline().split()))
    val = ba[m]
    answer = 0
    level = 9
    while True:
        for i in range(len(ba)):
            if ba[i] == level:
                ba = ba[:i] + ba[i+1]
                answer += 1

        else:
            level -= 1