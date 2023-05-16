# 2805_농작물수확하기

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    r, c = N // 2, N // 2
    queue = deque()
    queue.append((r, c, farm[r][c]))
    visited = {(r, c)}
    ans = 0

    for _ in range(int((1/2) * (N ** 2) + 1/2)):
        r, c, crops = deque.popleft(queue)
        ans += crops

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                queue.append((nr, nc, farm[nr][nc]))
                visited.add((nr, nc))

    print(f'#{tc} {ans}')