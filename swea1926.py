# 220519
# 간단한 369게임
# 규칙1. 숫자 1부터 순서대로 차례대로 말하되, '3, '6', '9'가 들어가 있는 수는 말하지 않는다.
# 규칙2. 해당 수들을 말하지 않는 대신, 박수를 친다. 이 때, 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다. ex) 36은 박수를 두번 쳐야 한다.
# 입력으로 정수 N이 주어졌을 때, 1 ~ N까지의 숫자를 게임 규칙에 맞게 출력하는 프로그램
# 박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 '-'를 출력
# N은 10 이상 1,000 이하의 정수

n = int(input())

for i in range(1, n + 1):
    num = list(map(int, str(i)))
    cnt = 0
    if 3 in num or 6 in num or 9 in num:
        cnt += num.count(3)
        cnt += num.count(6)
        cnt += num.count(9)
        print('-' * cnt, end=' ')
    else:
        print(i, end=' ')