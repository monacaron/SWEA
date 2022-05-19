# 220519
# 최빈수 구하기
# 최빈수를 출력하는 프로그램 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수 출력)
# 학생의 수는 1,000명이며, 각 학생의 점수는 0점 이상 100점 이하의 값
import sys
from collections import Counter
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

t = int(input()) # 테스트 케이스의 개수

for test_case in range(1, t + 1):
    n = int(input()) # 테스트 케이스 번호
    num = list(map(int, input().split()))
    count = Counter(num).most_common()
    print(f'#{n} {count[0][0]}')
