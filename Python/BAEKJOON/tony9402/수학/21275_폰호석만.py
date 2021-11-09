import sys
sys.stdin = open("21275in.txt",'r')

li = list(sys.stdin.readline().split())
a = []
if li[0].isalpha():
    for j in li[0]:
        a.append(ord(j)-87)
else:
    a.append(int(li[0]))
print(a)