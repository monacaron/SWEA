# 보트의 특정값과 학생들의 몸무게가 주어졌을 때, 조건을 만족하는 4명의 학생을 선택하는 프로그램
# 각 반에서 한 명씩 선출하여 몸무게 합이 특정값에 근사
# 근사값이 여러 개일 때, 더 작은 값을 선택

# 입력1) 테스트 케이수 개수 T
# 입력2) 특정값 k, 각 반의 학생 수 n (1 <= k <= 40,000,000, 1 <= n <= 1,000. k, n은 정수)
# 입력3) 4개의 줄에 차례로 각 반의 학생들의 몸무게를 n개씩 입력. 몸무게는 1 이상 10,000,000 이하

# 출력 : 카누 선수로 지목된 학생들의 몸무게의 총합

# 바이너리 인덱스 트리 이용

import sys
sys.stdin = open("input.txt", "r")
INF = int(1e9)

t = int(input())

for test_case in range(1, t + 1):
    k, n = map(int, input().split())
    body = []
    for _ in range(4):
        body.append(list(map(int, input().split())))
    # one = 1반 + 2반
    # two = 3반 + 4반
    one, two = [], []
    for i in range(n):
        for j in range(n):
            one.append(body[0][i] + body[1][j])
            two.append(body[2][i] + body[3][j])

    # 크기 순으로 정렬
    one.sort()
    two.sort()

    # 투포인터
    result = 0
    diff = INF
    i, j = 0, len(two) - 1
    # 각각의 포인터가 범위를 벗어나지 않도록
    while i < len(one) and 0 <= j:
        tmp = one[i] + two[j] - k # 선택된 학생들의 몸무게 총 합 - 특정값
        if abs(tmp) < diff:
            diff = abs(tmp)
            result = tmp + k
        elif abs(tmp) == diff: # 근사값이 여러 개인 경우, 더 작은 수를 선택
            result = min(result, tmp + k)

        if tmp < 0:
            i += 1
        elif tmp > 0:
            j -= 1
        else:
            break

    print(result)