# 공격 역할 A팀, 방어 역할 B팀 ~ 총 n명
# 참가자는 1 ~ n 번호. Ai, Bi는 양의 정수로 참가자 i의 공격 능력과 방어 능력
# n명의 참가자를 팀 A와 팀 B로 아래 조건을 지키면서 나누어야 한다.
# 조건1) 두 팀에 배정된 참가자 수의 차이는 k 이하
# 조건2) 각 참가자는 두 팀 중 하나에 반드시 속함
# 조건3) 위의 두 조건을 만족하는 모든 팀 배정 방법 중, 팀 A에 배정된 참가자들의 공격 능력 총 합과 팀 B에 배정된 참가자들의 방어 능력치 총 합이 최대가 되어야 함
# n, k, 참가자의 공격/방어 능력치가 주어졌을 때, 가능한 모든 팀 배정 방식 중에서 능력치 합의 최댓값 구하기
# 1 <= T <= 10, 3 <= n <= 100,000, 1 <= k <= n - 2, 1 <= Ai, Bi <= 1,000,000

# 입력1) 테스트 케이스 개수 T
# 입력2) 총 참가자 수 n, 팀원 차이 제한 k
# 입력3) 참가자의 공격 능력 A1, A2, ..., An
# 입력4) 참가자의 방어 능력 B1, B2, ..., Bn

# 출력 : 각 테스트 케이스 마다 능력치 합의 최댓값을 한 줄에 하나씩 출력

# 공격 능력치와 방어 능력치 중 큰 값을 sum에 더해줌
# 공격과 방어의 차이를 더 큰 능력치의 리스트에 저장 ~ 공격이 클 경우 a, 방어가 클 경우 b
# a, b를 오름차순으로 정렬
# a와 b의 길이차가 k보다 크다면, sum에서 한 개씩 빼주기. b에서 빼면 a는 1 증가

import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    nums = [i for i in range(1, n + 1)] # 참가자 번호

    attack = list(map(int, input().split())) # 공격 능력치
    defense = list(map(int, input().split())) # 방어 능력치

    A = []
    B = []
    sum = 0
    # 팀 배정 경우의 수
    # 팀원 수의 차이는 k 이하
    # 각 참가자는 반드시 두 팀 중 하나에 소속

    for i in range(n):
        if attack[i] > defense[i]:
            sum += attack[i]
            A.append(attack[i] - defense[i])
        else:
            sum += defense[i]
            B.append(defense[i] - attack[i])

    A.sort()
    B.sort()
    a = len(A)
    b = len(B)

    idx= 0
    while abs(a - b) > k:
        if a > b:
            sum -= A[idx]
            a -= 1
            b += 1
        else:
            sum -= B[idx]
            b -= 1
            a += 1
        idx += 1

    print(sum)