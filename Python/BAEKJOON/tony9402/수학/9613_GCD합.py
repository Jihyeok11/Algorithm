import sys
sys.stdin = open("9613in.txt", 'r')

def gcd(a, b):
    if not b:
        return a
    return gcd(b, a%b)

for _ in range(int(sys.stdin.readline())):
    li = list(map(int, sys.stdin.readline().strip().split()))
    c = li[0]
    li = sorted(li[1:], key=lambda x:-x)
    answer = 0
    for i in range(c-1):
        for j in range(i+1, c):
            answer += gcd(li[i], li[j])
    print(answer)