# 5250_최소비용

import heapq

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

for tc in range(1, int(input()) + 1):
    N = int(input())
    # 각 지점의 높이가 담긴 원본 지도
    field = [list(map(int, input().split())) for _ in range(N)]
    # 각 지점까지 드는 연료양이 기록될 비용 지도
    fuel = [[987654321] * N for _ in range(N)]
    fuel[0][0] = 0

    # 검토 지점이 들어오고 나갈 힙큐 리스트
    queue = []

    # 초기값 입력(해당 지점까지 소요되는 연료, r좌표, c좌표)
    heapq.heappush(queue, (0, 0, 0))

    # 큐가 빌 때까지
    while queue:
        # 값을 꺼내서
        cnt, current_r, current_c = heapq.heappop(queue)

        # 4방 탐색
        for d in range(4):
            nr, nc = current_r + dr[d], current_c + dc[d]
            # 지도를 벗어나는 경우는 제외
            if 0 <= nr < N and 0 <= nc < N:
                # 임시값을 구하여
                tmp = cnt + max(0, field[nr][nc] - field[current_r][current_c]) + 1
                # 임시값이 다음 지점 현재 최소값보다 작은 경우에는 비용 지도를 갱신하고 힙큐에 추가
                if tmp < fuel[nr][nc]:
                    fuel[nr][nc] = tmp
                    heapq.heappush(queue, (tmp, nr, nc))
                # 임시값이 현재 최소값보다 크다면 힙큐에 추가되지 않으므로 지도의 모든 부분이 최소화되면 자연스럽게 힙큐도 비게 됨

    # 정답은 비용 지도의 도착지 값
    ans = fuel[N - 1][N - 1]
    print(f'#{tc} {ans}')