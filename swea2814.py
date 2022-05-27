# 220527
# 최장 경로
# N개의 정점과 M개의 간선으로 구성된 가중치가 없는 무방향 그래프에서의 최장 경로의 길이를 계산하는 프로그램
# 정점의 번호는 1번부터 N번까지 순서대로 부여
# 경로에는 같은 정점의 번호가 2번 이상 등장 X
# 경로 상의 인접한 점들 사이에는 반드시 두 정점을 연결하는 간선 존재
# 경로의 길이는 경로 상에 등장하는 정점의 개수

# 입력1) 테스트 케이스 개수 T
# 입력2) N M (1 <= N <= 10, 0 <= M <= 20)
# 입력3) M개의 줄에 걸쳐서 그래프의 간선 정보를 나타내는 두 정수 x, y(1 <= x, y <= N)
# x, y는 서로 다른 정수이며, 두 정점 사이에 여러 간선이 존재할 수 있음

# 출력 : #t + 그래프에서의 최장 경로

def dfs(idx, ans):
    global result

    visited[idx] = 1 # 해당 idx 방문 처리

    ans += 1 # 경로 +1

    if result < ans: # 최종 결과가 ans보다 작으면
        result = ans # 최종 결과 갱신. 전역 함수라 갱신 가능
    for i in graph[idx]: # 연결된 노드 중
        if visited[i] == 0:  # 아직 방문하지 않은 곳으로 이동
            dfs(i, ans)
    visited[idx] = 0 # 모든 과정 수행 후 다음 수행을 위해 방문 노드 초기화

import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)] # 1번부터 N번까지
    visited = [0 for _ in range(n + 1)] # 해당 노드의 방문 여부
    for _ in range(m): # 간선 정보 입력
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    result = 0
    for i in range(1, n + 1): # 시작 노드를 다르게. 1번 ~ N번
        dfs(i, 0)

    print(f'#{test_case} {result}')