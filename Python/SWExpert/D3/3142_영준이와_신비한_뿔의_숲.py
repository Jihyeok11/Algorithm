import sys
sys.stdin = open("3142in.txt",'r')

for Count in range(int(input())):
    N,M = map(int,input().split()) # N은 뿔의 개수, M은 마리 수
    Answer = 2*M - N # 전부 트윈 혼일때 뿔 개수 - 부족한 뿔 개수 = 유니콘 수
    print("#{} {} {}".format(Count+1,Answer,M-Answer)) 
