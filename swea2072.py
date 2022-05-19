# 220519
# 홀수만 더하기
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    nums = list(map(int, input().split()))
    result = 0
    for num in nums:
        if num % 2 != 0:
            result += num

    print(f'#{i+1} {result}')