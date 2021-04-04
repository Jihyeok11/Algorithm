import sys
sys.stdin = open("1865in.txt",'r')

Answer = 0
Max = total = 0

def bubun(idx):
    global Max, total
    if idx == N:
        if total > Max:
            Max = total
        else:
            return
            
    else:
        for i in range(N):
            if use_check[i] == True:
                use_check[i] = False
                total *= (max(List[idx][i],0.001) / 100)
                bubun(idx+1)
                total /= (max(List[idx][i],0.001) / 100)
                use_check[i] = True
    

T = int(input())
T = 10
for Count in range(T):
    N = int(input())
    List = [ list(map(int,input().split())) for _ in range(N) ]
    Max = 0
    total = 1
    use_check = [True] * N
    bubun(0)
    print("#{0} {1:0.6f}".format(Count+1, Max*100))