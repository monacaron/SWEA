# 220519
# 달팽이 숫자
# 달팽이는 1부터 N * N까지의 숫자가 시계방향응로 이루어져 있다.
# 정수 N을 입력 받아 N크기의 달팽이를 출력하는 프로그램
# 달팽이의 크기 N은 1 이상 10 이하의 정수
import sys
#sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

t = int(input()) # 테스트 케이스의 개수

for test_case in range(1, t + 1):
    n = int(input()) # 테스트 케이스 N
    snail = [[0 for _ in range(n)] for _ in range(n)]

    # [0]은 좌우, [1]은 상하
    # flag = 0 ~ 좌우, flag = 1 ~ 상하
    direct = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 우(0) > 하(1) > 좌(3) > 상(4)
    num, flag = 1, 0 # 현재 숫자, 방향 flag
    r, c = 0, 0 # 현재 위치 / 행r열c

    while num <= n * n:
        snail[c][r] = num
        num += 1

        # 다음 위치
        check_r = r + direct[flag][0]
        check_c = c + direct[flag][1]

        # 변경 위치가 범위를 벗어나는 경우, flag 변경
        # 이미 숫자가 있는 경우, flag 변경
        if check_r <0 or check_r >= n or check_c < 0 or check_c >= n or snail[check_c][check_r]:
            flag = (flag+1) % 4

        r += direct[flag][0]
        c += direct[flag][1]

    print(f'#{test_case}')
    for row in snail:
        print(*row)