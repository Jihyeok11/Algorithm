import sys, bisect
from collections import defaultdict
sys.stdin = open("23939in.txt", 'r')

problem = defaultdict(list)
for _ in range(int(sys.stdin.readline())):
    p,l = map(int, sys.stdin.readline().split())
    problem[l].append(p)
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    if s[0] == "a":
        a, p, l = s.split()
        problem[int(l)].append(int(p))
    elif s[0] == "r":
        a, w = s.split()
        if int(w) == 1:
            Max = 0
            for i in problem.keys():
                if i > Max:
                    Max = i
            print(max(sorted(problem[Max], key=lambda x:x)))
        else:
            Min = 10**10
            for i in problem.keys():
                if i < Min:
                    Min = i
            print(min(sorted(problem[Min], key=lambda x : x)))
    elif s[0] == "s":
        a, w = s.split()
        # print(w)
print(problem)