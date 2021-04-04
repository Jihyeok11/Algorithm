import sys
sys.stdin = open("1747in.txt",'r')

n = int(sys.stdin.readline())
decimal = [True] * 1050001
decimal[1] = False
def my_decimal():

    for i in range(2,len(decimal)):
        if decimal[i]:
            for j in range(2*i,len(decimal),i):
                decimal[j] = False
my_decimal()
def my_palindrome(n):
    while True:
        if str(n) == str(n)[::-1]:
            if decimal[n]:
                return n
        n += 1
print(my_palindrome(n))