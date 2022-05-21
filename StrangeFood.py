# 코스 음식 중 몇 개만 골라서 싱거운 음식으로 시작해서 점점 짜게 먹다가 어느 순간부터 점점 싱겁게 먹으려고 한다.
# 각 음식의 염도가 순서대로 주어질 때, 위와 같이 먹으면 최대 몇 개를 먹을 수 있는지 구하는 프로그램
# 단, 음식이 식기 전에 먹어야 하므로 음식의 순서를 임의로 바꿔서 먹을 수 없으며, 증가하는 부분이나 감소하는 부분이 없어도 된다.
# ex) 1 9 8 3 6 3 9 5 1 4 2 >>> 1 9 8 6 5 4 2
# 1번) 98 2 37 5 12
# 2번) 23 32 12 98 3 2 1 9 6 2 12 32 12 3 4 8 45 2 3 21
# 3번) 32 12 98 3 86 42 23 12 2 1 9 6 2 12 32 12 3 2 8 45 2 3 21 37 92 53 68 49 13 87
# 정방향 LIS + 역방향 LIS 최댓값
import sys
# input = sys.stdin.readline

t = int(input()) # 테스트 케이스 개수

for test_case in range(1, t + 1):
    foods = list(map(int, input().split()))
    n = len(foods)

    dp1 = [1 for _ in range(n)] # LIS 정방향
    dp2 = [1 for _ in range(n)] # LIS 역방향

    for i in range(1, n):
        for j in range(0, i):
            if foods[j] <= foods[i]:
                dp1[i] = max(dp1[i], dp1[j] + 1)

    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if foods[j] <= foods[i]:
                dp2[i] = max(dp2[i], dp2[j] + 1)
    dp = []
    for i in range(n):
        dp.append(dp1[i] + dp2[i])

    print(max(dp))