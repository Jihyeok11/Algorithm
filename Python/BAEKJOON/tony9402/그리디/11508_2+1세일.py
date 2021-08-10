import sys
sys.stdin = open("11508in.txt", 'r')

n = int(sys.stdin.readline().strip())
li = sorted(list(int(sys.stdin.readline().strip()) for _ in range(n)), key=lambda x:x, reverse=True)
total = 0
for i in range(0, n, 3):
    total += sum(li[i:i+2])
print(total)