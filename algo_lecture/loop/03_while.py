# while 반복문의 기본 구조
nums = [1, 2, 3, 4, 5]

i = 0
while i < 5:
    print(nums[i])
    i += 1

# 조건문을 활용한 필터
i = 0
while i < 5:
    if nums[i] % 2 == 0:
        print(nums[i])
    i += 1

# 무한 루프(증감식)
num = 0
while i <5:
    print(num)

while True:
    print("무한루프")
    break