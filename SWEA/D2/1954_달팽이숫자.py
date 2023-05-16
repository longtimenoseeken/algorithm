# 1954_달팽이숫자
# 우 하 좌 상

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

for tc in range(1, int(input()) + 1):
    N = int(input())

    matrix = [[0] * N for _ in range(N)]
    r, c, d = 0, 0, 0

    for num in range(1, N ** 2 + 1):
        matrix[r][c] = num

        nr, nc = r + dr[d], c + dc[d]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or matrix[nr][nc] != 0:
            d = (d + 1) % 4
            nr, nc = r + dr[d], c + dc[d]

        r, c = nr, nc

    print(f'#{tc}')
    for ans in matrix:
        print(*ans)