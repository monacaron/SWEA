# 숫자 n을 3의 거듭제곱 숫자들을 중복 없이 더해서 만들 수 있는지 구하는 프로그램
# 1도 3^0으로 3의 거듭제곱으로 본다.
# ex) 109 = 3^0 + 3^3 + 3^4 ~ 가능
# ex) 7 = 3^0 + 3^1 + 3^1 ~ 3^1 중복 ~ 불가능
# 3진법으로 표현 후 2가 있으면 불가능

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    result = []
    while n > 3:
        result.append(n % 3)
        n //= 3

    result.append(n)

    if 2 in result:
        print(False)
    else:
        print(True)