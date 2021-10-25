import sys
sys.stdin = open("9251in.txt", 'r')

a = list(sys.stdin.readline().strip())
b = list(sys.stdin.readline().strip())

li = list(list(0 for _ in range(len(a)+1)) for _ in range(len(b)+1))
for y in range(1, len(b)+1):
    for x in range(1, len(a)+1):
        if a[x-1] == b[y-1] and flag:
            flag = 0
            li[y][x] = max(li[y-1][x], li[y][x-1]) + 1
        else:
            li[y][x] = max(li[y-1][x], li[y][x-1])
# print(li[-1][-1])
print(li)