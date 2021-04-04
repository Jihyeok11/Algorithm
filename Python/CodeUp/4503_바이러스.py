import sys
sys.stdin = open("in.txt",'r')

def vir(idx):
    for i in basket[idx]:
        if not i in box:
            box.append(i)
            vir(i)

    
N = int(input())
pair = int(input())
basket = {}
for i in range(N):
    basket[i+1] = []
    
for i in range(pair):
    fr,ed = map(int,input().split())
    basket[fr].append(ed)
    basket[ed].append(fr)
# print(basket) {1: [2, 5], 2: [1, 3, 5], 3: [2], 4: [7], 5: [1, 2, 6], 6: [5], 7: [4]}
box = [1]
vir(1)
print(len(box)-1)