# 220523
# [S/W 문제해결 기본] 1일차 - Flatten
# 평탄화 : 높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업
# 평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램

# 제약사항
# 가로 길이는 항상 100
# 모든 위치에서 상자의 높이는 1 이상 100 이하
# 덤프 횟수는 1이상 1 이상 1000 이하
# 주어진 덤프 횟수 이내에 평탄화가 완려되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차 반환(주어진 데이터에 따라 0 or 1)

# 입력1) 10개의 테스트 케이스. 각 테스트 케이스의 첫 번째 줄에는 덤프 횟수
# 입력2) 다음 줄에 상자의 높이값

# 출력 : #n + 최고점과 최저점의 높이 차

import sys
sys.stdin = open("input.txt", "r")

def dump(arr):
    global count

    if count == n:
        return

    xnum = max(arr)
    nnum = min(arr)
    if abs(xnum - nnum) > 1:
        count += 1
        xindex = arr.index(xnum)
        nindex = arr.index(nnum)

        arr[xindex] -= 1
        arr[nindex] += 1

        dump(arr)

    else:
        return

for test_case in range(1, 11):
    n = int(input()) # 덤프 횟수
    height = list(map(int, input().split()))

    count = 0

    dump(height)

    result = abs(max(height) - min(height))

    print(f'#{test_case} {result}')