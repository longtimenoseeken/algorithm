# 1206_view

for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    ans = 0

    i = 2
    while i < N-2:
        l2, l1, m, r1, r2 = buildings[i-2:i+3]
        max_height = max(l2, l1, r1, r2)
        if m > max_height:
            ans += m - max_height
            i += 3

        i += 1

    print(f'#{tc} {ans}')