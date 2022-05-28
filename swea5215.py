# 220528
# 햄버거 다이어트
# 햄버거 재료에 대한 점수와 가에에서 제공하는 재료에 대한 칼로리가 주어졌을 때, 좋아하는 햄버거를 먹으면서도 다이어트에 성공할 수 있도록 정해진 칼로리 이하의 조합 중에서 가장 선호하는 햄버거를 조합해주는 프로그램
# 여러 재료를 조합하였을 때 햄버거의 선호도는 조합된 재료들의 맛에 대한 점수의 합으로 결정
# 같은 재료를 여러 번 사용할 수 없음
# 조합 제한은 칼로리를 제외하고는 없음

# 입력1) 테스트 케이스 개수 T
# 입력2) 재료의 수 N, 제한 칼로리 L (1 <= N <= 20, 1 <= L <= 10^4)
# 입력3) N개의 줄에 재료에 대한 맛 점수와 칼로리를 나타내는 Ti, Ki (1 <= Ti <= 10^3, 1 <= Ki <= 10^3)

def func(idx, s, cal):
    global result
    global score
    global count

    if idx > n - 1:
        return

    if score < s + t[idx] and cal + k[idx] <= l:
        score = s + t[idx]
        result = cal + k[idx]

    func(idx + 1, s + t[idx], cal + k[idx])
    func(idx + 1, s, cal)

import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case in range(1, t+1):
    n, l = map(int, input().split()) # 재료의 수, 제한 칼로리
    t = [] # 맛 점수
    k = [] # 칼로리

    result = 0
    score = 0
    for _ in range(n):
        x, y = map(int, input().split())
        t.append(x)
        k.append(y)
    count = 0
    func(0, 0, 0)

    print(f'#{test_case} {score}')