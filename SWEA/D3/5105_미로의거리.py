# 5105_미로의거리

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

for tc in range(1, int(input()) + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    current = deque()
    visited = set()

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                current.append((0, r, c))
                visited.add((r, c))

    ans = 0

    while current:

        cnt, r, c = current.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or (nr, nc) in visited or maze[nr][nc] == 1:
                continue

            if maze[nr][nc] == 3:
                ans = cnt
                break

            current.append((cnt + 1, nr, nc))
            visited.add((nr, nc))


    print(f'#{tc} {ans}')