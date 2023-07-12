# 5102_노드의거리
from collections import deque

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    matrix = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        r, c = map(int, input().split())
        matrix[r][c], matrix[c][r] = 1, 1

    S, G = map(int, input().split())
    current = deque()
    visited = set()
    current.append((0, S))
    visited.add(S)

    ans = 0

    while current:
        cnt, node = current.popleft()
        if node == G:
            ans = cnt
            break

        for i in range(V + 1):
            if matrix[node][i] == 1 and i not in visited:
                current.append((cnt + 1, i))
                visited.add(i)

    print(f'#{tc} {ans}')