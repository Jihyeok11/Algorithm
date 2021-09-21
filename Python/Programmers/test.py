a = [7, 2, 3, 8, 4, 5 ]
dp = [0] * len(a)

for i in range(1, len(a)):
    for j in range(i - 1, -1, -1):
        if a[i] > a[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
print(dp)
Max = 0
for i in range(len(dp)):
    if Max < dp[i]:
        Max = dp[i]
print(Max)