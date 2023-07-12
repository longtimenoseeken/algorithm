# 5188_최소합

#우, 하
dr = (0, 1)
dc = (1, 0)

def solution(r, c, cnt):
    global ans
    
    # 백트래킹: 중간합이 현재 최소합보다 큰 경우 더 이상 탐색하지 않습니다.
    if cnt > ans:
        return
    
    # 종착지에 도착한 경우 ans를 갱신하고 return합니다.
    if (r, c) == (N - 1, N - 1):
        ans = min(ans, cnt)
        return
    
    # 정해진 방향으로 2방 탐색하며 재귀를 돕니다.
    for d in range(2):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            solution(nr, nc, cnt + matrix[nr][nc])

for tc in range(1, int(input()) + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    ans = 13 * 13 * 10

    solution(0, 0, matrix[0][0])

    print(f'#{tc} {ans}')