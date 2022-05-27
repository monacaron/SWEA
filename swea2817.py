# 220527
# 부분 수열의 합
#  A1, A2, ..., An의 N개의 자연수가 주어졌을 때, 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하는 프로그램

# 입력1) 테스트 케이스 개수 T
# 입력2) N K (1 <= N <= 20, 1 <= K <= 1,000)
# 입력3) N개의 자연수 수열 A (1 이상 100 이하)

# 출력 : #t +  부분 수열의 합이 K가 되는 경우의 수

def func(idx, result):
    global cnt

    if idx >= n:
        return

    result += nums[idx]

    if result == k:
        cnt += 1


    # 현재 nums[idx]를 선택하는 경우
    func(idx+1, result)
    # 현재 numx[idx]를 선택하지 않는 경우
    func(idx+1, result - nums[idx])

import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    cnt = 0
    func(0, 0)

    print(f'#{test_case} {cnt}')