import sys
sys.stdin = open("1110in.txt",'r')

def cycle(n):
    a = n//10
    b = n%10
    c = (a+b)%10
    return b*10+c

n = int(sys.stdin.readline())
number = n
cnt = 0
while True:
    cnt += 1
    result = cycle(number)
    if n == result:
        print(cnt)
        break
    else:
        number = result
        