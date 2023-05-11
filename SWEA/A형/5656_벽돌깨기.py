# 벽돌 깨기

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# depth == 구슬 개수 카운팅 cnt == 현 시점에서 깨진 벽돌 카운팅, matrix == 대상 이차원 행렬
def dfs(depth, cnt, matrix):
    global total, broken

    if cnt == total: # depth 끝나기 전에 다 깨지면 return
        broken = cnt
        return
    
    if depth == N: # depth 끝나면(구슬 다 쏘면) broken 최신화하여 return
        broken = max(broken, cnt)
        return
    
    for c in range(W): # 열 하나씩 모두 검토
        arr = [x[:] for x in matrix] # deepcopy
        stack = set() # 이번 라운드에 깨질 벽돌들 보관할 스택
        tmp = 0 # tmp == 이번 라운드에 깨질 벽돌들 숫자 카운팅

        for r in range(H): # 해당 열 맨 위에 있는 벽돌 스택에 추가
            if arr[r][c]:
                stack.add((r, c))
                break

        while stack: # 스택이 빌 때까지 이번 라운드 진행
            r, c = stack.pop() # 꺼내서
            if arr[r][c]: # 해당 위치 숫자가 0이 아니면
                tmp += 1 # tmp에 1 추가하고
                for d in range(4): # 4방탐색하며 (벽돌에 적힌 숫자-1) 범위에 있는 좌표들 모두 스택에 추가
                    nr, nc = r, c
                    for _ in range(arr[r][c] - 1):
                        nr, nc = nr + dr[d], nc + dc[d]
                        if 0 <= nr < H and 0 <= nc < W:
                            stack.add((nr, nc))
                arr[r][c] = 0 # 꺼낸 벽돌 깨기

        # 벽돌 다 깨고 정렬하는 로직
        for x in range(W): # 각 열에서
            i = H - 1 # 기준은 맨 아래
            for y in range(H -1, -1, -1): # 맨 아래부터 검토
                if arr[y][x]:
                    arr[i][x], arr[y][x] = arr[y][x], arr[i][x]
                    i -= 1 # 교환했으면 기준 하나 올리기
        
        dfs(depth + 1, cnt + tmp, arr) # (depth에 1 추가, cnt에 tmp 추가, 깨고 정렬한 이차원 리스트) 로 재귀

for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]

    total = 0
    for r in range(H): # 총 벽돌 수 카운팅
        for c in range(W):
            if matrix[r][c]:
                total += 1

    broken = 0
    dfs(0, 0, matrix) # dfs 돌며 가장 많이 깨지는 경우의 깨진 벽돌 수 카운팅

    ans = total - broken # 정답은 남은 벽돌 수

    print(f'#{tc} {ans}')