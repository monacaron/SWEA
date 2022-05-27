# 220527
# 파리 퇴치
# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수
# M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리 죽이기
# 5 <= N <= 15, 2 <= M <= N
# 각 영역의 파리 갯수는 30 이하

# 입력1) 테스트 케이스 개수 T
# 입력2) N M
# 입력3) N줄에 걸쳐 N x N 배열 입력

# 출력 : #t + 최대 파리 수

import sys
sys.stdin = open("input.txt", "r")

def kill(row, col, m):
    result = 0
    for i in range(m):
        for j in range(m):
            result += matrix[row + i][col + j]

    return result

t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())

    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    result = 0
    for row in range(n - m + 1):
        for col in range(n - m + 1):
            result = max(result, kill(row, col, m))

    print(f'#{test_case} {result}')