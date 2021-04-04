N = 5
List_A = [[_ for _ in range(N)] for _ in range(N)]
List = List_A[:]
List = [[_+1 for _ in range(N)] for _ in range(N)]
print(List)
print(List_A)