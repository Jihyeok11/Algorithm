import sys
sys.stdin = open("11000in.txt" ,'r')

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    a, b = map(int,sys.stdin.readline().strip().split())
    li.append((a, b))
li = sorted(li, key= lambda x : x[1], reverse = True)
li = sorted(li, key= lambda x : x[0])
time = 1
cnt = 0
for a, b  in li:
    if time in range(a, b+1):
        print(a, b)
        time = b
        cnt += 1
print(cnt)