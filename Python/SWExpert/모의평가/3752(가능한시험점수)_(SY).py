import sys
sys.stdin = open("3752in.txt",'r')

T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    scores = sorted(list(map(int, input().split())))
    dp = 1
    for e in scores:
        dp = dp << e | dp
        # print(bin(dp))
 
    cnt = 0
    for e in bin(dp):
        if e == '1':
            cnt += 1
 
    print('#%d'%test_case,cnt)