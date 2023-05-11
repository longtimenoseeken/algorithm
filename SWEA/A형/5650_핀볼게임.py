# 핀볼 게임

# 상 - 하 - 좌 - 우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
change = ((1, 0, 3, 2), (1, 3, 0, 2), (3, 0, 1, 2), (2, 0, 3, 1), (1, 2, 3, 0), (1, 0, 3, 2))

def check(r, c, d):
    global ans
    R, C = r, c
    cnt = 0

    while True:
        r, c = r + dr[d], c + dc[d]
        if not (0 <= r < N and 0 <= c < N):
            d = change[0][d]
            cnt += 1
        elif matrix[r][c] == -1 or (r, c) == (R, C):
            break
        elif 1 <= matrix[r][c] <= 5:
            d = change[matrix[r][c]][d]
            cnt += 1
        elif 6 <= matrix[r][c] <= 10:
            r, c = wormhole[(r, c)]
    
    ans = max(cnt, ans)

for tc in range(1, int(input()) + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    tmp = dict()
    wormhole = dict()
    for r in range(N):
        for c in range(N):
            if 6 <= matrix[r][c] <= 10:
                if matrix[r][c] in tmp:
                    wormhole[tmp[matrix[r][c]]] = (r, c)
                    wormhole[(r, c)] = tmp[matrix[r][c]]
                else:
                    tmp[matrix[r][c]] = (r, c)

    for r in range(N):
        for c in range(N):
            if not matrix[r][c]:
                for d in range(4):
                    check(r, c, d)

    print(f'#{tc} {ans}')