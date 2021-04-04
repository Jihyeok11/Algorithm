memo = {}
total = 0
def Memo(k,n):
    if k ==0:
        return n
    if k != 0:
        memo[(k,n)] = memo[(k-1,n)] 



def my_sum(k,n):
    global total
    if n==0:
        return 0
    if (k,n) not in memo:
        while k != 0:
            memo((k,n)) += 




    Memo(k,n) = 0
print(my_sum(2,3))


memo = {1:1, 2:1}
def fibonacci(n):
    if n == 0:
        return 0
    if n not in memo:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]