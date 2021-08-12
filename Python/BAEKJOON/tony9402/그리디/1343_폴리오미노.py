import sys
sys.stdin = open("1343in.txt", 'r')


word = sys.stdin.readline().strip()
word = word.replace("XXXX", "AAAA").replace("XX", "BB")
if ("X" in word):
    print(-1)
else:
    print(word)