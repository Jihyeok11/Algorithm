from math import gcd
def solution(w,h):
    answer = 0
    GCD = gcd(w,h)
    rect = GCD * (w//GCD + h//GCD - 1)
    return w*h-rect

W = 8
W = 100000000
H = 12
H = 999999999
W,H = 8,12
W,H = 6,4
W,H = 100000000,999999999


print(solution(W,H))