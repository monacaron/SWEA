# 220528
# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는  프로그램
# 진짜 일곱 난쟁이의 키의 합은 100

# 입력 : 아홉 개의 줄에 걸쳐 난쟁이들의 키 입력
# 주어지는 키는 100을 넘지 않는 자연수이며, 모두 다르다.
# 가능한 정답이 여러 가지인 경우에는 아무거나 출력

# 출력 : 일곱 난쟁이의 키를 오름차순으로 출력
# 일곱 난쟁이를 찾을 수 없는 경우는 x

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

all = sum(dwarfs)

result = []
for i in range(8):
    for j in range(i + 1, 9):
        if all - dwarfs[i] - dwarfs[j] == 100:
            result.append([i, j])

x = result[0][0]
y = result[0][1]
if x > y:
    x, y = y, x

dwarfs.remove(dwarfs[x])
dwarfs.remove(dwarfs[y - 1])
dwarfs.sort()

for i in dwarfs:
    print(i)