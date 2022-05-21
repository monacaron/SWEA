# 고양이는 무조건 한 시간에 한 번 이동하고, 예상대로 움직인다고 할 때, M시간 뒤에 고양이가 있는 위치를 구하는 프로그램
# 고양이의 이동 방법은 다음과 같다.
# 2 4 1 5 3
# 위와 같이 주어진다면 1 > 2 / 2 > 4 / 3 > 1 / 4 > 5 / 5 > 3
# 해당 위치 > 이동 위치
# ex) 2 4 1 5 3, 8
# 고양이의 시작 위치는 1이고, 다음과 같이 8번 이동
# 1 - 2 - 4 - 5 - 3 - 1 - 2 - 4 - 5 ~ 즉, 5가 정답
# 순환 규칙

t = int(input()) # 테스트 케이스 개수

for test_case in range(1, t + 1):
    rule = [0] # 인덱스 1부터 규칙이 시작하도록
    rule += list(map(int, input().split()))

    m = int(input()) # 이동 시간

    idx = 1
    cycle = [1]
    for i in range(m - 1): # 시작은 1로 고정. 이후 m - 1번 이동
        if rule[idx] in cycle:
            break
        cycle.append(rule[idx])
        idx = rule[idx]

    m %= len(cycle)

    print(cycle[m])