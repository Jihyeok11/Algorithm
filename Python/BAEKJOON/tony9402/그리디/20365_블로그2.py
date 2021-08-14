import sys
sys.stdin = open("20365in.txt", 'r')

n = int(sys.stdin.readline())
li = list(x for x in sys.stdin.readline().strip())
word = li[0]
for i in li:
    if word[-1] != i:
        word += i
r = word.count("B")
print(min(r + 1, len(word) - r + 1))