# 5356_의석이의세로로말해요

for tc in range(1, int(input()) + 1):
    words = [input() for _ in range(5)]

    max_c = max(len(word) for word in words)

    ans = ''

    for c in range(max_c):
        for r in range(5):
            if c < len(words[r]):
                ans += words[r][c]

    print(f'#{tc} {ans}')