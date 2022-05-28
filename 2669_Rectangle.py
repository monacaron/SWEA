# 밑변이 모두 가로축에 평행한 네 개의 직사각형
# 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 포함할 수도 있으며, 변이나 꼭짓점이 겹칠 수 도 있음
# 해당 직사각형들이 차지하는 면적을 구하는 프로그램

# 입력 : 네 줄에 걸쳐 각 줄마다 직사각형의 위치를 나타내는 네 개의 정수 입력
# 첫 번째와 두 번째 정수는 사각형 왼쪽 아래 꼭짓점의 x, y 좌표
# 세 번째와 네 번째 정수는 사각형 오른쪽 위 꼭짓점의 x, y 좌표
# 모든 x, y 좌표는 1 이상 100 이하의 정수

# 출력 : 네 개의 직사각형이 차지하는 면적
# w = rec[][2] - rec[][0]
# h = rec[][3] - rec[][1]

# 100 x 100의 빈 테이블 생성
# 직사각형이 그려진 곳을 1로 갱신 ~ 값이 1인 칸의 개수 구하기

recs = []
for _ in range(4):
    recs.append(list(map(int, input().split())))

table = [[0 for _ in range(100)] for _ in range(100)]

for rec in recs:
    x1, y1, x2, y2 = rec[0], rec[1], rec[2], rec[3]
    for i in range(x1, x2):
        for j in range(y1, y2):
            table[i][j] = 1

result = 0
for i in range(100):
    for j in range(100):
        if table[i][j] == 1:
            result += 1

print(result)