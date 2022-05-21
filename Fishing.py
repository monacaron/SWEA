# n명의 사람이 일렬로 서서 낚시를 하고 있는데 낚싯줄이 서로 엉켜버렸다.
# 엉킨 낚시줄 몇 개를 잘라서 멀쩡한 낚싯줄만 남기려고 한다.
# 사람의 번호를 왼쪽부터 1 ~ n이라고 하고, 찌도 왼쪽 1 ~ n번째에 있다.
# 1번 사람부터 n번 사람까지의 찌가 몇 번째에 있는지 주어질 때, 최소 몇 개의 줄을 잘라야 하는지 구하여라.
# ex) 3 1 2 ~ 1번 사람의 낚싯줄을 끊으면 2, 3번 사람의 낚싯줄끼리는 엉키지 않으므로 하나만 자르면 된다.
# 1) 4 1 5 2 3
# 2) 5 4 3 2 1
# 3) 1 7 2 6 5 3 4
# 4) 10 8 9 3 7 1 2 5 4 6
# 5) 3 9 12 8 7 2 6 1 4 5 10 11
# 최장 증가하는 수열(LIS) 이용
# n - LIS

t = int(input())

for test_case in range(1, t + 1):
    rope = [0]
    rope += list(map(int, input().split()))
    n = len(rope)

    dp = [1 for _ in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            if rope[j] < rope[i]:
                dp[i] = max(dp[i], dp[j] + 1)



    print(dp)
    print(f'#{test_case} {n - max(dp) - 1}')