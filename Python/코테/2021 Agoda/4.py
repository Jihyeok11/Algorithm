import sys
sys.stdin = open("4in.txt",'r')

n, g = map(int, input().split())
vi = list(list(0 for _ in range(n)) for _ in range(n))
hc = list(0 for _ in range(n))

for _ in range(n-1):
    a, b, d = map(int,input().split())
    vi[a-1][b-1] = d
    vi[b-1][a-1] = d
for i in range(n):
    ba = [(i,0)]
    check = [i]
    while ba:
        c, d = ba.pop()
        for j in range(n):
            if vi[c][j] and (not j in check):
                vi[i][j] = d + vi[c][j]
                ba.append((j, d + vi[c][j]))
                check.append(j)
for _ in range(int(input())):
    s = input()
    if s[0] == "H":
        h, name, u, c = s.split()
        u = int(u)
        hc[u-1] = (name, int(c))
    else:
        q, v = s.split()
        v = int(v)
        min_cost = 10**10
        idx = 0
        for i in range(n):
            if hc[i]:
                cost = vi[v-1][i]*g + hc[i][1]
                if min_cost > cost:
                    min_cost = cost
                    idx = i
        print(hc[idx][0], min_cost)