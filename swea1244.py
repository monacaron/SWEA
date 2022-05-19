# 220519
# [S/W 문제해결 응용] 2일차 - 최대 상금
# 주어진 숫자판들 중에 두 개를 선택해서 정해진 횟수만큼 서로의 자리를 교환할 수 있다.
# 정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 큼액을 계산하는 프로그램
import sys
sys. stdin = open("input.txt", "r")
# input = sys.stdin.readline

t = int(input()) # 테스트 케이스의 수.

for test_case in range(1, t + 1):
    # 최대 10개의 테스트 케이스 입력
    num, n = input().split() # 숫자판과 교환 횟수 / 숫자판의 정보는 최대 자릿수 6의 정수형 숫자, 최대 교환 횟수는 10번
    n = int(n)
    num = list(num)
    max_v = 0
    cnt = 0

    def dfs(start, num):
        global max_v, cnt
        if cnt == n:
            max_v = max(max_v, int(''.join(num)))
            return

        for i in range(start, len(num)):
            for j in range(i + 1, len(num)):
                if num[i] <= num[j]:  # 동일값도 swap
                    num[i], num[j] = num[j], num[i]
                    cnt += 1
                    dfs(i, num)
                    num[i], num[j] = num[j], num[i]
                    cnt -= 1

    dfs(0, num)

    if max_v == 0:
        left_n = n - cnt
        if left_n % 2:
            num[-2], num[-1] = num[-1], num[-2]
        max_v = int(''.join(num))
    print(f'#{test_case} {max_v}')
