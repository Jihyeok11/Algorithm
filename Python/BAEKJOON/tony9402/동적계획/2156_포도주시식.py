import sys
sys.stdin = open("2156in.txt", 'r')

n = int(sys.stdin.readline())
li = list(int(sys.stdin.readline()) for _ in range(n))
result = [0, 0, 0] + li
for i in range(n):
    if i >= 2:
        result[i + 3] = max(result[i] + li[i - 1] + li[i], result[i + 1] + li[i], result[i + 2])
    elif i >= 1:
        result[i + 3] = max(result[i] + li[i - 1] + li[i], result[i + 2])
    else:
        result[i + 3] = li[i]
print(result[-1])