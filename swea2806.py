# 220523
# N-Queens
# N * N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램

# 입력1) 테스트 케이스의 개수 T
# 입력2) 각 테스트 케이스의 첫 번째 줄에 하나의 자연수 N(1 <= N <= 10) 입력

# 출력 : #n + 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수

# 해당 위치에 퀸을 놓을 수 있는지 판단
def isPromising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global result

    if x == n:
        result += 1
        return

    for i in range(n):
        row[x] = i
        if isPromising(x):
            dfs(x + 1)

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    row = [0 for _ in range(n)] # chess[x] = y : x번째 줄 y번 인덱스에 퀸이 있다. 0번째 줄, 0번 인덱스부터 시작

    result = 0

    dfs(0)
    print(f'#{test_case} {result}')