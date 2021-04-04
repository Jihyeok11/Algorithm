N = int(input())
Dict = {
    0:0,
    1:1,
    2:2
}
def rect(N):
    for i in range(3,N+1):
        Dict[i] = Dict[i-1] + Dict[i-2]
rect(N)
A = Dict[N]
print(A %10007)