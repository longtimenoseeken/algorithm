# 줄기세포 배양

import heapq

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    cell = [list(map(int, input().split())) for _ in range(N)]
    cell_list = set()
    activate = []
    tmp = []

    for r in range(N):
        for c in range(M):
            if cell[r][c] != 0:
                heapq.heappush(activate, (-cell[r][c], r, c, 0))
                cell_list.add((r, c))

    for _ in range(K):
        while activate:
            x, r, c, t = heapq.heappop(activate)
            x = -x

            # 비활성화 -> t 1 추가해서 다시 넣기
            if t < x:
                heapq.heappush(tmp, (-x, r, c, t+1))

            # 활성화 -> 사방 탐색해서 갈 수 있으면 확장
            if x <= t < (2 * x):
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if (nr, nc) not in cell_list:
                        heapq.heappush(tmp, (-x, nr, nc, 0))
                        cell_list.add((nr, nc))
                if t + 1 < 2 * x:
                    heapq.heappush(tmp, (-x, r, c, t+1))
        activate = tmp[:]
        tmp = []

    ans = len(activate)
    print(f'#{tc} {ans}')