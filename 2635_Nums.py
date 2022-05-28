n = int(input())

result = []

if n == 1:
    print(4)
    print(1, 1, 0, 1)
else:
    for i in range(n // 2, n):
        nums = [n]
        nums.append(i)
        tmp = n - i
        while tmp >= 0:
            top = nums[-1]
            nums.append(tmp)
            tmp = top - tmp

        if len(result) < len(nums):
            result = nums[::]

    print(len(result))
    print(*result)

    11055_LIS.py
    2309_SevenDwarfs.py
    2635_Nums.py
    2669_Rectangle.py

    swea1220.py
    swea1225.py
    swea5215.py


