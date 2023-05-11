# 디저트 카페

# 좌하 - 우하 - 좌상 - 우상(방향 순서 고정)
dr = (1, 1, -1, -1)
dc = (-1, 1, 1, -1)

def dfs(r, c, d, cnt):
    global ans
    
    if d == 3 and (r, c) == (sr, sc):
        ans = max(ans, cnt)
        return
    
    if 0 <= r < N and 0 <= c < N and local[r][c] not in visited:
        nr, nc = r + dr[d], c + dc[d]
        visited.append(local[r][c])
        dfs(nr, nc, d, cnt + 1)
        visited.pop(-1)

        if d < 3:
            nr, nc = r + dr[d + 1], c + dc[d + 1]
            visited.append(local[r][c])
            dfs(nr, nc, d + 1, cnt + 1)
            visited.pop(-1)

for tc in range(1, int(input()) + 1):
    N = int(input())
    local = [list(map(int, input().split())) for _ in range(N)]

    ans = -1

    for r in range(N):
        for c in range(N):
            sr, sc = r, c
            visited = []
            dfs(r, c, 0, 0)

    print(f'#{tc} {ans}')