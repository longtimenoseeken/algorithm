# 4875_미로

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c):
    global ans
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or (nr, nc) in visited or maze[nr][nc] == 1:
            continue
        if maze[nr][nc] == 0:
            visited.append((nr, nc))
            dfs(nr, nc)
        elif maze[nr][nc] == 3:
            ans = 1
            return

for tc in range(1, int(input()) + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr, sc = r, c
                break

    ans = 0
    visited = []
    dfs(sr, sc)

    print(f'#{tc} {ans}')