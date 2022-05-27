# 220523
# 숫자가 같은 배수
# 자연수 N의 10진법 표기에서 나타나는 숫자들을 재배열하여 N보다 큰 N의 배수를 만들 수 있는지 판단하는 프로그램

# 입력1) 테스트 케이스의 개수 T
# 입력2) T개의 줄에 자연수 N(1 <= N <= 10^6)

# 출력 : 주어진 자연수에 나타난 숫자들을 재배열하여 더 큰 배수를 만들 수 있다면 'possible', 불가능하다면 'impossible' 출력

t = int(input())

for test_case in range(1, t + 1):
    n = input()
    num = int(n)

    n_list = list(map(str,n))
    n_list.sort()

    for i in range(2, 10):
        k = list(map(str, str(i * num)))

        if len(k) > len(n):
            result = 'impossible'
            break
        k.sort()

        if n_list == k:
            result = 'possible'
            break
        else:
            result = 'impossible'

    print(f'#{test_case} {result}')