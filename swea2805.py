# 220527
# 농작물 수확하기
# N x N 크기의 농장
# 규칙1) 농장의 크기는 항상 홀수이다.
# 규칙2) 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.
# 농장의 크기 N과 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수  있는 수익은 얼마인지 구하는 프로그램

# 농장의 크기 N은 1 이상 49 이하의 홀수
# 농작물의 가치는 0 이상 5 이하

# 입력1) 테스트 케이스의 개수 T
# 입력2) 농장의 크기 N
# 입력3) N개의 줄에 N개의 농작물의 가치를 공백없이 입력

# 출력 : #t + 수익
def product(farm, n):
    if n == 1:
        return farm[0][0]

    row = 0
    col = n // 2

    result = farm[row][col]

    start = col - 1
    end = col + 1
    while start >= 0 and end <= n - 1:
        row += 1
        line = farm[row][start:end + 1]
        result += sum(line)
        start -= 1
        end += 1

    start += 2
    end -= 2

    while start != end:
        row += 1
        line = farm[row][start:end + 1]
        result += sum(line)
        start += 1
        end -= 1

    result += farm[row + 1][end]
    return result


import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case in range(1, t + 1):
    n = int(input()) # 농장의 크기

    farm = [] # 농작물의 가치
    for _ in range(n):
        farm.append(list(map(int, input())))

    result = product(farm, n)

    print(f'#{test_case} {result}')