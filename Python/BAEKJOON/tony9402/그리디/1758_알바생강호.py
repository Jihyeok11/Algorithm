import sys
sys.stdin = open("1758in.txt", 'r')

n = int(sys.stdin.readline().strip())
li = sorted(list(int(sys.stdin.readline().strip()) for _ in range(n)), key= lambda x:x, reverse=True)
tip = 0
for i in range(n):
    tip += max(0, li[i] - i)
print(tip)