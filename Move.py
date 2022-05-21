# 2 * m 행렬의 (1, 1)에서 시작
# 행렬의 각 칸에는 그 칸을 지날 때의 점수가 적혀 있다.
# (1, 1)에서 오른쪽, 아래 방향으로만 이동해 (2, m) 위치로 이동하려고 할 때, 얻을 수 있는 최대 점수를 구하는 프로그램
# ex) 1  2  3
# ex) 10 5  6
# 맵이 위와 같이 주어진다면, 1 > 6 이동, 최대 점수는 1 + 10 + 5 + 6 = 22
# DP 이용

t = int(input()) # 테스트 케이스 개수

for test_case in range(1 , t + 1):
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    matrix = [l1, l2]

    dp = [[l1[0]], [l1[0] + l2[0]]]

    # 윗 라인
    # 오른쪽으로 가는 경우
    for i in range(1, len(l1)):
        dp[0].append(dp[0][i - 1] + l1[i])

    # 아래 라인
    for i in range(1, len(l2)):
        dp[1].append(max(dp[0][i] + l2[i], dp[1][i -1] + l2[i]))

    print(dp[1][len(l2) - 1])

