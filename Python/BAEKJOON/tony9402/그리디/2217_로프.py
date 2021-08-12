import sys
sys.stdin = open("2217in.txt",'r')

n = int(sys.stdin.readline())
li = sorted(list(int(sys.stdin.readline()) for _ in range(n)), key=lambda x:x, reverse=True)
k = Max = 0
for i in range(len(li)):
    k += 1
    if k * li[i] > Max:
        Max = k * li[i]
print(Max)