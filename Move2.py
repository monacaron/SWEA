# 2 * m 행렬의 (1, 1)에서 시작
# 행렬의 각 칸에는 그 칸을 지날 때의 점수가 적혀 있다.
# (1, 1)에서 오른쪽, 아래 방향으로만 이동해 (2, m) 위치로 이동하려고 할 때, 얻을 수 있는 최대 점수를 구하는 프로그램
# ex) 1  2  3
# ex) 10 5  6
# 맵이 위와 같이 주어진다면, 1 > 6 이동, 최대 점수는 1 + 10 + 5 + 6 = 22
# 누적 합 이용

t = int(input())

for test_case in range(1, t + 1):
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    up = [l1[0]] # l1 누적 합
    down = [l2[-1]] # l2 누적 합

    for i in range(1, len(l1)):
        up.append(up[i - 1] + l1[i])
        down.append(down[i - 1] + l2[len(l2) - i - 1])

    down.reverse()

    result = []
    for i in range(0, len(l1)):
        result.append(up[i] + down[i])

    print(max(result))