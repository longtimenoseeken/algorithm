# 홈 방범 서비스

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    house = []
    ans = 0

    for r in range(N):
        for c in range(N):
            if city[r][c] == 1:
                house.append((r, c))

    for r in range(N):
        for c in range(N):
            distance = []
            for (y, x) in house:
                distance.append(abs(r-y) + abs(c-x) + 1)
            K = max(distance)
            for k in range(K, 0, -1):
                cnt = 0
                for d in distance:
                    if d <= k:
                        cnt += 1
                if (cnt * M) - (k * 2 * (k - 1) + 1) >= 0:
                    ans = max(cnt, ans)
                    break

    print(f'#{tc} {ans}')