# 1949_등산로 조성

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, cnt, construction):
    global ans

    # ans 비교하여 큰 값으로 최신화
    ans = max(ans, cnt)

    # 사방 탐색
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        # 맵 벗어나거나 visited에 있으면 넘어감
        if nr < 0 or nr >= N or nc < 0 or nc >= N or (nr, nc) in visited:
            continue
        # 이동할 수 있으면 visited 넣고 다음으로 이동(나올 때 visited에서 pop)
        elif mount[nr][nc] < mount[r][c]:
            visited.append((nr, nc))
            dfs(nr, nc, cnt + 1, construction)
            visited.pop()
        # 이동할 수 없으면 공사해보기
        elif mount[nr][nc] >= mount[r][c] and not construction:
            for i in range(1, K+1):
                mount[nr][nc] -= i
                construction = True
                if mount[nr][nc] < mount[r][c]:
                    visited.append((nr, nc))
                    dfs(nr, nc, cnt + 1, construction)
                    visited.pop()
                construction = False
                mount[nr][nc] += i

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    mount = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 봉우리 값 찾기
    H = 0
    for r in range(N):
        for c in range(N):
            H = max(H, mount[r][c])

    # 봉우리 찾아서 탐색 시작
    for r in range(N):
        for c in range(N):
            if mount[r][c] == H:
                visited = []
                visited.append((r, c))
                dfs(r, c, 1, False)

    print(f'#{tc} {ans}')