# 5251_최소이동거리

def find(current, cnt):
    global ans

    # 백트래킹: 중간값이 현재 최소값보다 크다면 해당 방향 탐색 중단
    if cnt > ans:
        return

    # 목적지에 도착하면 ans 갱신 후 return
    if current == V:
        ans = min(ans, cnt)
        return

    # 현재 지점에서 다음에 갈 곳 탐색, cnt에 거리 더하고 재귀
    for next in range(V + 1):
        if city[current][next] <= 10:
            find(next, cnt + city[current][next])

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    # 주어진 간선 정보를 인접 행렬로 정리, 연결되지 않은 곳은 매우 큰 수로 채우기
    city = [[9876543210] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        city[s][e] = w

    ans = 987654321

    find(0, 0)

    print(f'#{tc} {ans}')