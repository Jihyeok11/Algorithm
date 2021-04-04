N = int(input())
List = [ [ 0 for _ in range(10)] for _ in range(101) ]

for i in range(1,10):
    List[1][i] = 1

for i in range(2,N+1):
    for j in range(0,10):
        if j == 0:
            List[i][j] = List[i-1][1]
        elif j== 9:
            List[i][j] = List[i-1][8]
        else:
            List[i][j] = List[i-1][j-1] + List[i-1][j+1]

print(sum(List[N]) % 1000000000)