# 두 문자열 A, B가 주어진다.
# 문자열 A에 할 수 있는 연산은 다음 두 가지가 있다.
# 연산1) 문자 하나를 지운다
# 연산2) 문자 하나를 추가한다.
# A를 B와 같아지게 하려면 위 연산을 최소 몇 번 해야 하는지 구하여라.
# LCS : 최대 공통 부분 수열

t = int(input()) # 테스트 케이스 개수

for test_case in range(1, t + 1):
    A, B = input().split()

    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    lcs = dp[len(A)][len(B)] # 최대 공통 부분 수열
    f1 = len(A) - lcs # 연산1 횟수
    f2 = len(B) - lcs # 연산2 횟수

    print(f1 + f2)