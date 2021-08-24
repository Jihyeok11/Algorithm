import sys
sys.stdin = open("2141in.txt", 'r')

n = int(sys.stdin.readline())
town = list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(n))
# town = sorted(list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)), key=lambda x:x[0])
print(town)
people = 0
for i in range(n):
    people += town[i][1]
count = 0
for i in range(n):
    count += town[i][1]
    if count >= round(people/2):
        print(town[i][0])
        break