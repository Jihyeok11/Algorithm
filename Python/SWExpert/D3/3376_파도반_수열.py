import sys
sys.stdin = open("3376in.txt",'r')

List = [1,1,1,2,2]
for Count in range(int(input())):
    Number = int(input())
    if Number>len(List):
        for _ in range(Number-len(List)):
            List.append(List[len(List)-1] + List[len(List)-5])
    print("#{} {}".format(Count+1,List[Number-1]))