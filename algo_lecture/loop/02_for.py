# for 반복문의 기본 구조
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
word = "PYTHON"

for num in nums:
    print(num)

for character in word:
    print(character)

# for 반복문 주의 사항
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:
    print(num + 1)

    # 변수를 수정해도 원본 컨테이너는 그대로
print(nums)

    # 반복문이 종료되어도 여전히 변수에 원소가 할당되어 있음
print(num)

    # 조건문을 활용한 필터
for num in nums:
    if num % 2 == 0:
        print(num)

# for 반복문에서 range 자료형 활용
    # range를 활용한 N회 반복
for _ in range(3):
    print("이 문장은 3회 반복됩니다.")

    # 변수를 인덱스로 활용하여 컨테이너 원소에 접근
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

for i in range(5):
    print(nums[i])

        # 컨테이너 원소를 직접 수정할 수 있음
nums = [1, 2, 3, 4, 5]

for i in range(5):
    nums[i] += 1

print(nums)

        # 두 개 이상 컨테이너에 동시에 접근할 때 유용
nums_1 = [1, 3, 5, 7, 9]
nums_2 = [2, 4, 6, 8, 10]

for i in range(5):
    print(nums_1[i] + nums_2[i])

# 2중 for 문
for num_1 in nums_1:
    for num_2 in nums_2:
        print(num_1, num_2)

    # 2중 for 문을 활용한 이차원 리스트 탐색
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

        # 행 우선 순회
for r in range(3):
    for c in range(4):
        print(matrix[r][c])

        # 열 우선 순회
for c in range(4):
    for r in range(3):
        print(matrix[r][c])