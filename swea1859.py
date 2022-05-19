# 220519
# 백만 장자 프로젝트
# 다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주는 프로그램
# 조건1. 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
# 조건2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
# 조건3. 판매는 얼마든지 할 수 있다.
import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

t = int(input()) # 테스트 케이스의 수 T

for test_case in range(1, t + 1):
    n = int(input()) # 2 <= N <= 1,000,000
    price = list(map(int, input().split())) # 각 날의 매매가. 총 N개. 10,000이하
    result = 0 # 최대 이득

    sale = price[-1] # 마지막 판매가
    # 뒤에서부터 탐색
    for i in range(n - 1, 0, -1):
        if sale > price[i - 1]:
            result += sale - price[i - 1]
        else:
            sale = price[i - 1]

    print(f'#{test_case} {result}')
