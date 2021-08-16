import sys
sys.stdin = open("21758in.txt", 'r')

n = int(sys.stdin.readline().strip())
honey = list(map(int, sys.stdin.readline().strip().split()))
li = []
ans = 0
# 벌통을 가운데에 뒀을 때
a = sum(honey[1 : n-1]) + max(honey[1 : n-1])
# 벌통을 왼쪽에 뒀을 때
left = l_total = sum(honey[1:n])
l_max = r_max = 0
for i in range(1, n-1):
    l_total -= 2 * honey[i]
    if l_max < l_total:
        l_max = l_total
    l_total += honey[i]
# 벌통을 오른쪽에 뒀을 때
right = r_total = sum(honey[0:n-1])
for i in range(n-2, -1, -1):
    r_total -= 2 * honey[i]
    if r_max < r_total:
        r_max = r_total
    r_total += honey[i]
print(max(a, l_max + left, r_max + right))