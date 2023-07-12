# 5178_노드의합

def tree(idx):
    parent = idx
    child = parent * 2

    ars[parent] = ars[child] + ars[child + 1]

    if idx == 1:
        return
    
    tree(idx - 1)

for tc in range(1, int(input()) + 1):
    N, M ,L = map(int, input().split())
    ars = [0] * (N + 1)

    for _ in range(M):
        c, n = map(int, input().split())
        ars[c] = n

    if N % 2:
        ars[N // 2] = ars[N] + ars[N - 1]
    else:
        ars[N // 2] = ars[N]

    tree((N // 2)-1)
    ans = ars[L]

    print(f'#{tc} {ans}')