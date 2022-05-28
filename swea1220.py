# 220528
# [S/W 문제해결 기본] 5일차 - Magnetic
# 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수를 구하는 프로그램
# 테이블의 크기는 100 x 100
# 자성체는 테이블 앞뒤쪽에 있는 N극 또는 S극에만 반응하며 자성체끼리는 반응 x

# 입력1) 정사각형 테이블의 한 변의 길이
# 입력2) 총 10개의 테스트 케이스
# 1 = N극 자성체, 2 = S극 자성체
# 테이블의 윗 부분에 N극, 아랫 부분에 S극이 위치한다고 가정

# 출력 : #t + 교착 상태의 개수

import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 10 + 1):
    n = int(input()) # 한 변의 길이 / 100으로 고정
    table =[]

    # 테이블 정보 입력
    for _ in range(100):
        table.append(list(map(int, input().split())))

    # 윗쪽 S극 제거
    for i in range(100):
        for j in range(100):
            if table[j][i] == 1:
                break
            if table[j][i] == 2:
                table[j][i] == 0
    # 아래쪽 N극 제거
    for i in range(99, -1, -1):
        for j in range(99, -1, -1):
            if table[j][i] == 2:
                break
            if table[j][i] == 1:
                table[j][i] == 0

    lines = [[] for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if table[j][i] != 0:
                lines[i].append(table[j][i])
    result = 0
    for line in lines:
        for i in range(len(line) - 1):
            if line[i] == 1 and line[i + 1] == 2:
                result += 1

    print(f'#{test_case} {result}')