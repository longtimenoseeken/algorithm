# 2001_파리퇴치

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    flies = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for r in range(N - M + 1):
        for c in range(N - M + 1):
            cnt = sum(flies[y][x] for y in range(r, r + M) for x in range(c, c + M))
            ans = max(cnt, ans)

    print(f'#{tc} {ans}')