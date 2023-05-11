# break의 활용
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)
    if num == 3:
        print("반복을 종료합니다.")
        break

# 이중 for 문에서 break 사용
nums_1 = [1, 3, 5, 7, 9]
nums_2 = [2, 4, 6, 8, 10]

for num_1 in nums_1:
    for num_2 in nums_2:
        print(num_1, num_2)

        if num_2 == 6:
            print("num_2가 6을 초과하여 종료")
            break
    print("하지만 위에 있는 for 반복문은 계속됩니다.")

# continue 활용
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in nums:
    if not num % 2:
        continue
    if not num % 3:
        continue

    print(num)

# continue 왜 씀?
for num in nums:
    if num % 2 and num % 3:
        print(num)