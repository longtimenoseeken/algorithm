# 탈주범 검거

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    ug = [list(map(int, input().split())) for _ in range(N)]
    queue = deque()
    timer = 0

    # 출발지 큐에 집어넣기
    queue.append((timer, R, C))
    visited = set()

    while queue:

        timer, r, c = queue.popleft()

        if timer >= L:
            break

        else:
            visited.add((r, c))

            if ug[r][c] == 1:
                direction = [0, 1, 2, 3]

            elif ug[r][c] == 2:
                direction = [0, 1]
                
            elif ug[r][c] == 3:
                direction = [2, 3]

            elif ug[r][c] == 4:
                direction = [0, 3]

            elif ug[r][c] == 5:
                direction = [1, 3]

            elif ug[r][c] == 6:
                direction = [1, 2]

            elif ug[r][c] == 7:
                direction = [0, 2]

            for i in direction:
                nr, nc = r + dr[i], c + dc[i]

                if nr < 0 or nr >= N or nc < 0 or nc >= M or (nr, nc) in visited or ug[nr][nc] == 0:
                    continue

                elif i == 0 and ug[nr][nc] in [1, 2, 5, 6]:
                    queue.append((timer + 1, nr, nc))

                elif i == 1 and ug[nr][nc] in [1, 2, 4, 7]:
                    queue.append((timer + 1, nr, nc))

                elif i == 2 and ug[nr][nc] in [1, 3, 4, 5]:
                    queue.append((timer + 1, nr, nc))

                elif i == 3 and ug[nr][nc] in [1, 3, 6, 7]:
                    queue.append((timer + 1, nr, nc))

    ans = len(visited)
    print(f'#{tc} {ans}')