# 5247_연산

from collections import deque

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    queue = deque()
    queue.append((N, 0))
    visited = set()

    while True:
        num, cnt = deque.popleft(queue)

        if num == M:
            break

        if num >= 1000000 or num <= 0 or num in visited:
            continue

        visited.add(num)
        queue.append((num + 1, cnt + 1))
        queue.append((num - 1, cnt + 1))
        queue.append((num * 2, cnt + 1))
        queue.append((num - 10, cnt + 1))

    print(f'#{tc} {cnt}')