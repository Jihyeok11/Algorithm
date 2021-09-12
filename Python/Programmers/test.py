def rotate_90(n, List):
    cnt = 0
    l = len(List)
    li = list(list(0 for _ in range(l)) for _ in range(l))
    while cnt < n:
        for y in range(l):
            for x in range(l):
                li[x][l - 1 - y] = List[y][x]
        cnt += 1
        for y in range(l):
            for x in range(l):
                List[y][x] = li[y][x]
    return li


a = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate_90(1,a))
print(rotate_90(1,a))
print(rotate_90(1,a))
print(rotate_90(1,a))