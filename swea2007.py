# 220523
# 패턴 마디의 길이
# 패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램

# 각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.

# 입력1) 테스트 케이스의 개수 T
# 입력2) T개의 줄에 길이가 30인 문자열 입력

# 출력 : #t + 마디의 길이
import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for test_case in range(1, t + 1):
    string = input()

    for i in range(1, len(string)):
        result = string[0:i]
        if result == string[i: i + len(result)]:
            break
    print(f'#{test_case} {len(result)}')