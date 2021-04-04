import sys
sys.stdin = open("1244in.txt",'r')


def Todo(Try):
    global Max
    if Try:
        for i in range(len(List)-1):
            for j in range(i+1,len(List)):
                List[i],List[j] = List[j],List[i]
                Str = ''
                for m in List:
                    Str += str(m)
                Int = int(Str)
                if Int > Max:
                    Max = Int
                Todo(Try-1)
                List[i],List[j] = List[j],List[i]
    else:
        return Max
T = int(input())
for Count in range(T):
    print("#{0} ".format(Count+1),end='')
    Num,Try = map(int,input().split())
    List = []
    while Num>0:
        List.append(Num%10)
        Num //= 10
    List.reverse() #[1,2,3]
    Max = 0
    half = len(List)//2
    if half > Try:
        Todo(Try)
    elif half<=Try:
        Todo(half+1)
        List = []
        while Max>0:
            List.append(Max%10)
            Max //= 10
        List.reverse() #[1,2,3]
        for i in range(Try-half):
            List[-2],List[-1] = List[-1],List[-2]
        Str = ''
        for m in List:
            Str += str(m)
        Max = int(Str)
    print(Max)
    # List = []
    # while Num>0:
    #     List.append(Num%10)
    #     Num //= 10
    # List.reverse() #[1,2,3]
    # print(ABC)
