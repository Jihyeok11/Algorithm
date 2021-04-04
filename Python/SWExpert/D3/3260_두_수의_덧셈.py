import sys
sys.stdin = open("3260in.txt",'r')

List = []
for Count in range(int(input())):
    A,B = input().split()
    List.append(int(A)+int(B))

for i in range(len(List)):
    print("#{} {}".format(i+1,List[i]))
