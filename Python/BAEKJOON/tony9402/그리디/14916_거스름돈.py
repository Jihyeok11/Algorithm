import sys
sys.stdin = open("14916in.txt", 'r')

money = int(sys.stdin.readline())
total = money // 5
while total:
    cent = (money - total * 5)
    if cent % 2:
        total -= 1
    else:
        break
try:
    print(total + cent // 2)
except:
    print(-1)