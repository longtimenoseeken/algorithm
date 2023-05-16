# 1227_미로
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

for _ in range(10):
    tc = input()
    maze = [list(map(int, input())) for _ in range(100)]

    for r in range(100):
        for c in range(100):
            if maze[r][c] == 2:
                sr, sc = r, c
                break

    stack = deque()
    stack.append((sr, sc))
    visited = set()
    ans = 0

    while stack:
        r, c = stack.pop()
        if maze[r][c] == 3:
            ans = 1
            break

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= 100 or nc < 0 or nc >= 100 or (nr, nc) in visited or maze[nr][nc] == 1:
                continue

            else:
                stack.append((nr, nc))
                visited.add((nr, nc))

    print(f'#{tc} {ans}')