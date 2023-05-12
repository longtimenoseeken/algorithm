# 글자 수

for tc in range(1, int(input()) + 1):
    str1 = set(input())
    str2 = input()

    ans = 0

    for character in str1:
        cnt = str2.count(character)
        ans = max(ans, cnt)

    print(f'#{tc} {ans}')