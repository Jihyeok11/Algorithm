import sys
sys.stdin = open("12100in.txt",'r')

def cha(li,count):
    if count==2:
        return
    li[0][1] += 1
    cha(li,count+1)
    print(li)


n = int(sys.stdin.readline())
li = list(list(int(x) for x in sys.stdin.readline().split()) for _ in range(n))
# [[2, 2, 2], [4, 4, 4], [8, 8, 8]]
cnt = 0
cha(li,0)