# 4881_배열최소합

def perm(depth, cnt):
    global ans

    if cnt > ans:
        return

    if depth == N:
        ans = min(ans, cnt)
        return
    
    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            perm(depth + 1, cnt + matrix[depth][i])
            check[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N

    ans = 987654321

    perm(0, 0)

    print(f'#{tc} {ans}')