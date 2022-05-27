# 220527
# [S/W 문제해결 기본] 3일차 - 회문1
# 회문 : 거꾸로 읽어도 앞에서부터 읽은 것과 같은 문장이나 낱말
# 8 x 8 평면 글자판에서 가로, 세로를 모두 보아 제시된 길이를 가진 회문의 총 개수를 구하는 프로그램

# 입력1) 찾아야 하는 회문의 길이
# 입력2) 테스트 케이스

# 출력 : #t + 회문의 개수

import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 10 + 1):
    n = int(input())

    rec = []
    for _ in range(8):
        rec.append(input())

    result = 0

    # 가로
    for i in range(8):
        for j in range(8 - n + 1):
            word = rec[i][j:j + n]
            if word == word[::-1]:
                result += 1

    # 세로
    for i in range(8):
        for j in range(8 - n + 1):
            word = ''
            for k in range(j, j + n):
                word += rec[k][i]
            if word == word[::-1]:
                result += 1

    print(f'#{test_case} {result}')