import sys
sys.stdin = open("4676in.txt",'r')

T = int(input())
for Count in range(T):
    Str = [x for x in input()]
    String = [] # ['', 'w', '', 'o', '', 'w']
    for i in range(len(Str)):
        String += ['']+[Str[i]]
    String += ['']
    H = int(input())
    List = list(map(int,input().split()))
    for i in List:
        String[2*i] += '-'
    print("#{} {}".format(Count+1,''.join(String)))