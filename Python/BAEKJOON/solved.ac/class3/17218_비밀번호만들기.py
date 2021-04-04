import sys
sys.stdin = open("17218in.txt",'r')
import sys
def find_word(a,b):
    global ans
    if A[a]=="0" or B[b]=="0":
        return
    if li[a][b] == li[a][b-1]:
        find_word(a,b-1)
    elif li[a][b] == li[a-1][b]:
        find_word(a-1,b)
    else:
        ans += B[b]
        find_word(a-1,b-1)
B = sys.stdin.readline().strip()
A = sys.stdin.readline().strip()
A = "0"+A
B = "0"+B
li = list( list( 0 for _ in range(len(B))) for _ in range(len(A)))
for a in range(1,len(A)):
    for b in range(1,len(B)):
        if A[a]==B[b]:
            li[a][b] = li[a-1][b-1]+1
        else:
            li[a][b] = max(li[a-1][b],li[a][b-1])
ans = ""
find_word(len(A)-1,len(B)-1)
print(ans[::-1])