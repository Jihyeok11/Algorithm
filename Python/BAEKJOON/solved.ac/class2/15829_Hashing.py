import sys
sys.stdin = open("15829in.txt",'r')

n =int(sys.stdin.readline())
a = sys.stdin.readline().rstrip()
ans = 0
for i in range(n):
    m = ord(a[i])-96
    ans += (m*(31**i))
print(ans%1234567891)