import sys
sys.stdin = open("1759in.txt",'r')
import sys
l,c = map(int,sys.stdin.readline().split())
li = list(sys.stdin.readline().split())
vi = [True]*(c+1)
vowels = [97,101,105,111,117]
answer = []
def password(num):
    if len(num)==l:
        vowel = 0
        for i in num:
            if ord(i) in vowels:
                vowel += 1
        if vowel and len(num)-vowel>=2:
            answer.append(num)
        return
    for i in range(c):
        if vi[i]:
            if ord(li[i]) > ord(num[-1]):
                vi[i] = False
                password(num+li[i])
                vi[i] = True

for j in range(c):
    vi[j] = False
    password(li[j])
    vi[j] = True
answer.sort()
for i in answer:
    print(i)