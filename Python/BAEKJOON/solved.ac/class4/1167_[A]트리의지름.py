import sys
sys.stdin = open("1167in.txt",'r')

def get_farthest(i):
    farthest, dist = 0, 0    
    visit = [True] * (v+1)
    visit[i] = False
    stack = ba[i][:]
    
    for s in stack:
        visit[s[0]] = False
        if s[1] > dist:
            farthest = s[0]
            dist = s[1]
    
    while stack:
        bridge, now = stack.pop()
        for b in ba[bridge]:
            if visit[b[0]]:
                visit[b[0]] = False
                new = now + b[1]
                stack.append((b[0], new))
                if new > dist:
                    farthest = b[0]
                    dist = new
 
    return farthest, dist
            
v = int(sys.stdin.readline())
ba = {}
for _ in range(v):
    data = list(map(int, sys.stdin.readline().split()))
    ba[data[0]] = []
    for i in range(1, len(data)-1, 2):
        ba[data[0]].append((data[i], data[i+1]))
 
farthest, dist = get_farthest(1)
sys.stdout.write(str(get_farthest(farthest)[1]))