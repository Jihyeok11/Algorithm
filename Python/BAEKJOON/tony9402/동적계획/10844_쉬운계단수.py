import sys
sys.stdin = open("10844in.txt", 'r')

def stairs(n, num):
    global answer
    if len(num) == n:
        answer += 1
        return
    if int(num[-1]) == 0:
        stairs(n, num + "1")
    elif int(num[-1]) == 9:
        stairs(n, num + "8")
    else:
        stairs(n, num + str(int(num[-1]) + 1))
        stairs(n, num + str(int(num[-1]) - 1))
            

n = int(sys.stdin.readline())
answer = 0
for i in range(1, 10):
    stairs(n, str(i))
print(answer % 1000000000)