import sys
sys.stdin = open("21275in.txt",'r')
li = list(sys.stdin.readline().split())
nums = []
answer = []
def to_dec(word):
    res = []
    for i in word:
        if i.isalpha():
            res.append(ord(i)-87)
        else:
            res.append(int(i))
    return res

def phone_hosuck(nums):
    max_num = max(nums[0])
    res = []
    for i in range(max_num + 1, 36):
        n = 0
        for j in range(len(nums[0])):
            n += nums[0][len(nums[0]) - j - 1] * (i ** j)
        max_m = max(nums[1])
        for k in range(max_m+1, 36):
            cnt = 0
            tp = n
            flag = 1
            while tp > k:
                if (tp // k) == nums[1][cnt]:
                    cnt += 1
                    tp -= (tp//k) * k
                else:
                    flag = 0
                    break
            if tp != nums[1][cnt]:
                flag = 0
            if flag:
                res.append([n, i, k])
                if len(res) >= 2:
                    return "Multiple"
    if res:
        return " ".join(map(str, res[0]))

for i in li:
    nums.append(to_dec(i))
answer = phone_hosuck(nums)
if not answer:
    print("Impossible")
else:
    print(answer)