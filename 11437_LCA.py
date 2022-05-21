# 220521
# N (2 <= N <= 50,000)개의 정점으로 이루어진 트리
# 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번
# 두 노드의 쌍 M(1 <= M <= 10,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력하는 프로그램

# 입력1) 노드의 개수 N
# 입력2) N-1개 줄에는 트리 상에서 연결된 두 정점
# 입력3) 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M
# 입력4) M개 줄에는 정점 쌍이 주어짐

# 출력 : M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상 출력
import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(int(1e5))
LOG = 21 # 2^20 > 1,000,000

n = int(input()) # 노드의 개수
parent = [[0] * LOG for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
d = [0] * (n + 1) # 각 노드까지의 깊이
c = [0] * (n + 1) # 각 노트까지의 깊이가 계산되었는지 여부

for _ in range(n - 1): # 루트 노드는 부모x. 0 ~ n-2 = n-1개
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(x, depth): # 루트 노드부터 시작하여 깊이를 구하는 함수
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        parent[y][0] = x
        dfs(y, depth + 1)

# 전체 부모 관계를 설정하는 함수
# 2^i 부모 저장
def set_parent():
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1] # 노드 j의 2^i번째 부모


def lca(a, b): # A와 B의 최소 공통 조상을 찾는 함수
    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a

    # 먼저 깊이가 동일하도록
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]

    # 부모가 같아지도록
    if a == b:
        return a

    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]

set_parent()

m = int(input()) # 테스트 케이스 개수
for test_case in range(m):
    a, b = map(int, input().split()) # 공통 조상을 찾을 정점 쌍쌍
    print(lca(a, b))