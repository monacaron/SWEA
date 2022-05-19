# 220519
# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램
# 소수점 첫째 자리에서 반올림한 정수를 출력
# 각 수는 0 이상 10,000 이하의 정수
import sys
sys.stdin = open("input.txt", "r")

t = int(input()) # 테스트 케이스 개수

for test_case in range(1, t + 1):
    nums = list(map(int, input().split()))

    average = round(sum(nums) / 10)
    print(f'#{test_case} {average}')