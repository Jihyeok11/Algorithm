import sys
sys.stdin = open("9084in.txt", 'r')


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().strip().split()))[::-1]
    total = int(sys.stdin.readline())
    dp = list(0 for _ in range(total + 1))
    dp[0] = 1
    for coin in li:
        
        for i in range(1, total+1):
            if i - coin >= 0:
                dp[i] += dp[i - coin]
    print(dp[-1])