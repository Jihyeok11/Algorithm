import sys
sys.stdin = open("in.txt",'r')


import itertools
def get_store_dist(store_idxs):
    global min_store_dist,visited
    total_store_dist = 0
    visited = [True for _ in range(len(stores))]
    for house_r, house_c in houses:
        min_house_to_store = 1e9
        for idx in store_idxs:
            store_r, store_c = stores[idx]
            visited[idx] = False
            house_to_store = abs(house_r - store_r) + abs(house_c - store_c)
            min_house_to_store = min(min_house_to_store, house_to_store)
        total_store_dist += min_house_to_store
    if min_store_dist > total_store_dist:
        min_store_dist = total_store_dist
        my_sum = 0
        for idx in range(len(visited)):
            store_r, store_c = stores[idx]
            my_sum += stores_value[idx]
        min_store_dist += my_sum
    # min_store_dist = min(min_store_dist, total_store_dist)

for Count in range(int(input())):
    N = int(input())
    stores = []
    houses = []
    stores_value = []
    min_store_dist = 1e9
    for r in range(N):
        line = list(map(int, input().split()))
        for c in range(N):
            if line[c] == 1:
                houses.append((r, c))
            elif line[c] >= 2:
                stores.append((r, c))
                stores_value.append(line[c])
    # print(stores)
    visited = [True for _ in range(len(stores))]


    for i in range(1,len(stores)+1):
        for store_idxs in itertools.combinations(range(len(stores)), i):
            get_store_dist(store_idxs)
    print("#{} {}".format(Count+1,min_store_dist))

