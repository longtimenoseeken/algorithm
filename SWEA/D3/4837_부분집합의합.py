# 4837_부분집합의합

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = [x for x in range(1, 13)]

    ans = 0

    for i in range(1 << 12):
        selected = []
        for j in range(12):
            if i & (1 << j):
                selected.append(arr[j])
        if len(selected) == N and sum(selected) == K:
            ans += 1

    print(f'#{tc} {ans}')