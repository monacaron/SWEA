# 220527
# 파스칼의 삼각형
# 규칙1) 첫 번째 줄은 항상 숫자 1
# 규칙2) 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성
# N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램
# 1 <= N <= 10

# 입력1) 테스트 케이스 개수 T
# 입력2) N

# 출력1) #t
# 출력2) 파스칼의 삼각형

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    pascal = [[0 for j in range(i + 1)] for i in range(n)]
    pascal[0][0] = 1

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                pascal[i][j] = pascal[i - 1][j]
            elif j == i:
                pascal[i][j] = pascal[i - 1][j - 1]
            else:
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    print(f'#{test_case}')
    for i in range(n):
        for j in range(i + 1):
            print(pascal[i][j], end=' ')

        print()