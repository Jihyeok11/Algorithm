from collections import namedtuple
import sys
sys.stdin = open("3282in.txt",'r')


# item이라는 구조체 선언
item = namedtuple('item', ['w', 'v']);
UNDEFINED = -1;

# knapsack(n, c): n번 물건까지 c용량 만큼 남은 가방에 담을 수 있는 최대 가치를 구해주는 함수
def knapsack(n, c):
    # 이미 메모된 것이면 그것 사용
    if memo[n][c] is not UNDEFINED:
        return memo[n][c];

    # 물건이 더이상 없거나 가방에 더이상 담지 못하면 최대 가치는 0
    if n == 0 or c == 0:
        return 0;

    # 물건이 남은 용량보다 무거우면 이 물건을 담기 전 물건까지 구한 것이 최대가치
    if (items[n].w > c):
        return knapsack(n-1, c);

    # 위 케이스에 모두 해당 없다면, 현재 n번 물건을 넣었을 때와 넣지 않았을 때 최대가치를 각각 구해서 가치가 클 때를 택함
    resultA = items[n].v + knapsack(n-1, c-items[n].w);
    resultB = knapsack(n-1, c);

    if resultA > resultB:
        memo[n][c] = resultA;
        return resultA;
    else:
        memo[n][c] = resultB;
        return resultB;

given_tc = int(input());
for case_num in range(1, given_tc + 1):
    given_num, given_cap = map(int, input().split(' '));
    items = [item(0, 0)];
    memo = [[UNDEFINED for col in range(given_cap+1)] for row in range(given_num+1)]

    for i in range(0, given_num):
        w ,v = map(int, input().split(' '));
        items.append(item(w, v));

    print('#' + str(case_num) + ' ' + str(knapsack(given_num, given_cap)));