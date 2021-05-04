import sys
sys.stdin = open("2263in.txt",'r')

n = int(sys.stdin.readline())
inOrder = list(map(int,sys.stdin.readline().split()))
postOrder = list(map(int,sys.stdin.readline().split()))