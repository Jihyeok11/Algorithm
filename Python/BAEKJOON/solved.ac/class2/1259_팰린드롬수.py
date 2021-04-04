import sys
sys.stdin = open("1259in.txt",'r')
import sys
while True:
    a = sys.stdin.readline().strip()
    if not int(a):
        break
    elif a == a[::-1]:
        print("yes")
    else:
        print("no")