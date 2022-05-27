# 220527
# 스도쿠 검증
# 9 x 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 조건을 만족할 경우 1을 정답으로 출력하고 그렇지 않을 경우 0을 출력하는 프로그램
# 행, 열, 3 x 3 작은 격자에 1 ~ 9를 겹치지 않게 한 번 씩만 넣기

# 입력1) 테스트 케이스의 개수 T
# 입력2) 9 x 9 퍼즐 데이터

# 출력 : #t + 정답

import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case in range(1, t + 1):
    # 9 x 9 퍼즐 데이터 입력받기
    s = []
    for _ in range(9):
        s.append(list(map(int, input().split())))

    result = True # 조건 만족
    # 행 검사
    for i in range(9):
        if sum(s[i]) != 45:
            result = False
            break

    # 열 검사
    if result == True:
        for i in range(9):
            tmp = 0
            for j in range(9):
                tmp += s[j][i]
            if tmp != 45:
                result = False
                break

    # 3 x 3 격자 확인인
    if result == True:
        for i in range(0, 9, 3):
            tmp = 0
            for j in range(0, 9, 3):
                tmp = sum(s[i][j:j + 3]) + sum(s[i + 1][j:j + 3]) + sum(s[i + 2][j:j + 3])
            if tmp != 45:
                result = False
                break

    if result == True:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')