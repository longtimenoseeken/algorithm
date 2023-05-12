# 글자 수

from collections import Counter

for tc in range(1, int(input()) + 1):
    str1 = set(input())
    str2 = input()

    check = []

    for character in str2:
        if character in str1:
            check.append(character)

    counting = Counter(check).most_common()

    print(f'#{tc} {counting[0][1]}')