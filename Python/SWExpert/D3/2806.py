# import sys
# sys.stdin = open("2806in.txt",'r')

# T = int(input())
# for Count in range(T):
#     print("#{0} ".format(Count+1),end='')

#     N = int(input())
    
List=[[1,2,3],[4,5,6],[7,8,9]]
total = sum(sum(List,[]))
print(total)