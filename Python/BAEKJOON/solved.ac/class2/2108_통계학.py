import sys
sys.stdin = open("2108in.txt",'r')

import sys
# from collections import Counter
n = int(sys.stdin.readline())
li = sorted(list(int(input()) for _ in range(n)))
# print(li)
# 1. 산술 평균
def mean(nums):
    return round(sum(nums)/len(nums))

# a = (sum(li)/n)
# if a - int(a) >= 0.5:
#     print(int(a)+1)
# else:
#     print(int(a))

print(mean(li))
# 2. 중앙값
print(li[n//2])
# 3. 최빈값
def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()    
    
    if len(nums) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]

    return mod
print(mode(li))


# start = 5000
# myMax = 0
# res = 0
# maxNum = 0
# ba = []
# i = 0
# while i < len(li):
#     if start == li[i]:
#         res = 0
#         while i < len(li) and start == li[i]:
#             res += 1
#             i += 1
#         i -= 1
#         if res > myMax:
#             myMax = res
#             maxNum = li[i]
#             ba = [li[i]]
#         elif res == myMax:
#             if len(ba)<2:
#                 ba.append(li[i])
#     else:
#         start = li[i]
#         if not ba:
#             ba = [li[i]]
#     i += 1
# print(ba[0])
# 4. 범위
print(li[-1]-li[0])