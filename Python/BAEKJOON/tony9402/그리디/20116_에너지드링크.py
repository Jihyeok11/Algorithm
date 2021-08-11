import sys
sys.stdin = open("20115in.txt", 'r')


n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
Min = total = 0
for i in li:
    if i > Min:
        Min = i
    total += i

r = round(total/2 + Min/2, 1)
if (r - int(r)) > 0:
    print(r)
else:
    print(int(r))