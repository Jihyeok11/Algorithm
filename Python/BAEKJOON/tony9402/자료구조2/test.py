from collections import defaultdict


dfli = defaultdict(int)
for i in range(10):
    dfli[i] += i
print(dfli)
print(dfli[5])
print("-------------------------")

from bisect import bisect_left, bisect_right 

nums = [4, 5, 5, 5, 5, 5, 5, 5, 7, 6] 
n = 5 
print(bisect_left(nums, n)) 
a = bisect_right(nums, n)
print(nums[a])

