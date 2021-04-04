import sys
sys.stdin = open("1928in.txt",'r')   

T = int(input())
for Count in range(T):
    print("#{0} ".format(Count + 1),end = '')
    Str = input()
    Integer = ''

    for i in range(len(Str)):
        Int = ord(Str[i])               #2진법으로 변환
        if 65 <= Int <=90:              #A는 Base64
            A = Int - 65                
        elif 97 <= Int <= 122:
            A = Int - 71
        elif 48 <= Int <= 57:
            A = Int + 4
        B = bin(A)[2:]                  #B는 2진법으로
        B = str(B)
        
        while len(B)<6:
            B = '0'+B

        Integer += B
    D8 = ''
    for i in range(len(Integer)//8):
        A8 = str(Integer[8*i:8*(i+1)])  #A6는 6개씩 나눈값
        B8 = '0b'+A8
        C8 = int(B8,2)
        D8 += chr(C8)
    print(D8)


    # for i in range((len(Integer)//6)):
    #     A = str(Integer[6*i:6*(i+1)]) #6개씩 끊는다.
    #     B = '0b'+A                    #또 애들을 2진법으로 치환
    #     C = int(B,2)                  #10진법으로 치환
        
    #     if 0<= C <=25:
    #         D = chr(C+65)
    #     elif 26<= C <=51:
    #         D = chr(C+71)
    #     elif 52<= C <=63:
    #         D = chr(C-22)
    #     print(D,end='')

