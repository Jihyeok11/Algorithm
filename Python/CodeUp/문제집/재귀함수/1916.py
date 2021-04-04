memo = {1:1, 2:1}
def fibonacci(n):
    if n == 0:
        return 0
    if n not in memo:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]%10009

n = int(input())
print(fibonacci(n))