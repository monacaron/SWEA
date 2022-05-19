# 220519
# [S/W 문제해결 기본] 1일차 - View
# 좌우로 2칸 이상의 공백이 존재할 때 조망권이 확보됨
# 빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램
# 가로 길이는 항상 1000이하
# 맨 왼쪽 두 칸과, 맨 오른쪽 두 칸에는 건물 x
# 각 빌딩의 높이는 최대 255
import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

# 총 10개의 테스트 케이스
for testcase in range(1, 11):
    t = int(input())  # 테스트 케이스의 길이
    building = list(map(int, input().split())) # 빌딩의 높이
    result = 0
    for i in range(2, t - 2):
        left = max(building[i - 2], building[i - 1])
        right = max(building[i + 2], building[i + 1])
        if building[i] > left and building[i] > right:
            result += min(building[i] - left, building[i] - right)

    print(f'#{testcase} {result}')


