# 220527
# [S/W 문제해결 기본] 2일차 - Sum
# 100 x 100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램
# 총 10개의 테스트 케이스

# 입력1) 테스트 케이스 번호
# 입력2) 2차원 배열의 각 행 값

# 출력 : #t + 답

import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 10 + 1):
    dp1 = [0 for _ in range(100)] # 각 행의 합
    dp2 = [0 for _ in range(100)] # 각 열의 합
    left, right = 0, 0 # 각 대각선의 합

    t = int(input()) # 테스트 케이스의 번호

    matrix = []
    for _ in range(100):
        matrix.append(list(map(int, input().split())))

    for i in range(100):
        dp1[i] = sum(matrix[i])

    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += matrix[j][i]
        dp2[i] = tmp

    row, col = 0, 0
    while row < 100 and col < 100:
        left += matrix[row][col]
        row += 1
        col += 1

    row, col = 0, 99
    while row < 100 and col >= 0:
        right += matrix[row][col]
        row += 1
        col -= 1

    result = max(max(dp1), max(dp2), left, right)
    print(f'#{t} {result}')