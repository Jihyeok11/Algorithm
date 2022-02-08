import sys
sys.stdin = open("14467in.txt", 'r')

cows = dict()
answer = 0
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    if not a in cows:
        cows[a] = b
    else:
        if not cows[a] and b:
            cows[a] = b
            answer += 1
        elif cows[a] and not b:
            cows[a] = b
            answer += 1
print(answer)