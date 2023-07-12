# 5249_최소신장트리_프림

def prim():
    # 최소신장트리 하 인접 노트에서 해당 노드로 갈 때 최소 거리가 기록되는 리스트
    dist = [987654321] * (V + 1)
    # 임의의 출발지 선정(0번째 노드)
    dist[0] = 0
    visited = [False] * (V + 1)
    cnt = 0

    for _ in range(V + 1):
        min_idx = -1
        min_value = 987654321

        # 다음 방문지 탐색
        for i in range(V + 1):
            # 방문하지 않은 곳과 연결되는 간선 가운데 가장 짧은 간선을 선택
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]

        # 해당 노드로 이동하고
        visited[min_idx] = True
        # 해당 노드로 가는 간선의 가중치를 더하기
        cnt += min_value

        # 방문한 노드에서 연결된 간선들로 dist 정보 업데이트
        for i in range(V + 1):
            if not visited[i] and adj[min_idx][i] < dist[i]:
                dist[i] = adj[min_idx][i]
        print(dist)

    return cnt

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    adj = [[987654321] * (V + 1) for _ in range(V + 1)]

    # 가중치 정보를 인접 행렬로 정리
    for _ in range(E):
        r, c, w = map(int, input().split())
        adj[r][c], adj[c][r] = w, w

    ans = prim()

    print(f'#{tc} {ans}')