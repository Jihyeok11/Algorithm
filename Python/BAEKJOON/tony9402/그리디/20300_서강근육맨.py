import sys
sys.stdin = open("20300in.txt",'r')

n = int(sys.stdin.readline().strip())
li = sorted(list(map(int,sys.stdin.readline().strip().split())), key= lambda x:x)
Max = 0
if n%2:
    li.insert(0, 0)
for i in range(len(li)//2):
    r = li[i] + li[-(i+1)]
    if r > Max:
        Max = r
print(Max)