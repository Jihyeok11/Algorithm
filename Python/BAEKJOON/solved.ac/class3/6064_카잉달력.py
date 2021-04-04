import sys
sys.stdin = open("6064in.txt",'r')

# import sys

# def kaing(a):
#     if a%n == y or (a%n==0 and n==y):
#         return True
#     return False
# for _ in range(int(sys.stdin.readline())):
#     m,n,x,y = map(int,sys.stdin.readline().split())
#     s = x
#     while True:
#         if kaing(s):
#             break
#         s += m
#         if s>1600000000:
#             s = -1
#             break
#     print(s)
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    M, N, x, y = map(int, input().split())
    x, y = x - 1, y - 1
    ans = -1
    for i in range(x, M * N + 1, M):
        if i % N == y:
            ans = i + 1
            break
    print(ans)