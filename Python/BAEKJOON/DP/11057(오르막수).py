N = int(input())
List = [[0 for _ in range(10)] for _ in range(1001)]

for i in range(10):
    List[1][i] = 1
for i in range(2,N+1):
    for j in range(0,10,1):
        for k in range(j,10):
            List[i][j] += List[i-1][k]

print(sum(List[N]) % 10007)