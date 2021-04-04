import sys
sys.stdin = open("11650in.txt",'r')

n = int(sys.stdin.readline())
for i in sorted( list(list(map(int,sys.stdin.readline().split())) for _ in range(n)), key=lambda x:(x[0],x[1])):
    print("{} {}".format(i[0], i[1]))