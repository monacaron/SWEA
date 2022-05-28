# 220528
# 최장 증가 부분 수열
# 주어진 수열의 LIS의 길이를 계산한는 프로그램

# 입력1) 테스트 케이스 개수 T
# 입력2) 수열의 길이 N (1 <= N <= 1,000)
# 입력3) 수열의 원소 N개 (각 원소는 1 이상 2^31 - 1 이하의 자연수)

# 출력 : #t + LIS의 길이

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))

    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(f'#{test_case} {max(dp)}')