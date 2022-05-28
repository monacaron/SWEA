# 220528
# 가장 큰 증가 부분 수열
# 수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램

# 입력1) 수열 A의 크기 N (1 <= N <= 1,000)
# 입력2) 수열 A를 이루고 있는 Ai (1 <= Ai <= 1,000)

# 출력 : 수열 A의 합이 가장 큰 증가 부분 수열의 합

n = int(input())
nums = list(map(int, input().split()))

dp1 = [0 for _ in range(n)]
dp1[0] = 1
dp2 = nums[::]

for i in range(1, n):
    for j in range(0, i):
        if nums[j] < nums[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
            dp2[i] = max(dp2[j] + nums[i], dp2[i])

print(max(dp2))