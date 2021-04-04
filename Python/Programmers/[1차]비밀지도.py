import sys
sys.stdin = open("비밀지도in.txt",'r')
T = int(input())

n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
def solution(n, arr1, arr2):
    List1 = []
    for i in range(n):
        A = str(bin(arr1[i])[2:])
        if len(A)<n:
            A = (n-len(A))*'0'+A
            List1.append(A)
        else:
            List1.append(A)
    List2 =[]
    for i in range(n):
        A = str(bin(arr2[i])[2:])
        if len(A)<n:
            A = (n-len(A))*'0'+A
            List2.append(A)
        else:
            List2.append(A)
    print(List1)
    print(List2)
    answer = ['']*n
    for Y in range(n):
        Str = ''
        for X in range(n):
            if List1[Y][X] == '1' or List2[Y][X]=='1':
                Str+='#'
            else:
                Str += ' '
        answer[Y] = Str
    return answer

solution(n,arr1,arr2)