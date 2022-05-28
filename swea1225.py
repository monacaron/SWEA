# 220528
# [S/W 문제해결 기본] 7일차 - 암호생성기
# 다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.
# 1. 8개의 숫자 입력
# 2. 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
# 3. 다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다. ~ 1사이클
# 4. 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지, 프로그램 종료
# 총 테스트 케이스는 10개

# 입력1) 테스트 케이스의 번호
# 입력2) 8개의 데이터

# 출력 : #t + 정답

import sys
sys.stdin = open("input.txt", "r")

from collections import deque
for test_case in range(1, 10 + 1):
    t = int(input())
    nums = deque(map(int, input().split()))

    flag = 1 # 0이 되면 flag = 0
    cnt = 1
    while flag:
        if cnt > 5:
            cnt %= 5

        num = nums.popleft()
        num -= cnt

        if num <= 0:
            nums.append(0)
            break
        else:
            nums.append(num)
            cnt += 1

    result = list(nums)
    print(f'#{test_case}', end=' ')
    print(*result)