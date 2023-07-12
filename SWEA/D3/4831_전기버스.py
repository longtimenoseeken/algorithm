# 4831_전기버스

for tc in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split()))

    location = K
    ans = 0

    while location < N:
        for i in range(location, location - K, -1):
            if i in charges:
                ans += 1
                location = i
                break
        else:
            ans = 0
            break

        location += K

    print(f'#{tc} {ans}')