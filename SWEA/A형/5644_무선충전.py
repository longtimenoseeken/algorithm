# 무선 충전

dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

for tc in range(1, int(input()) + 1):
    M, N = map(int, input().split())
    A_trail = list(map(int, input().split()))
    B_trail = list(map(int, input().split()))
    AP = [list(map(int, input().split())) for _ in range(N)]
    AP = sorted(AP, key = lambda x : -x[3])
    ans = 0

    (ax, ay), (bx, by) = (1, 1), (10, 10)

    for time in range(M + 1):
        A_tmp = []
        B_tmp = []
        for i in range(len(AP)):
            if (abs(AP[i][0] - ax) + abs(AP[i][1] - ay)) <= AP[i][2]:
                A_tmp.append(i)
            if (abs(AP[i][0] - bx) + abs(AP[i][1] - by)) <= AP[i][2]:
                B_tmp.append(i)
        cnt = 0
        if A_tmp or B_tmp:
            if A_tmp and B_tmp:
                if A_tmp[0] == B_tmp[0]:
                    if len(A_tmp) > 1:
                        cnt = max(cnt, AP[A_tmp[1]][3] + AP[B_tmp[0]][3])
                    if len(B_tmp) > 1:
                        cnt = max(cnt, AP[A_tmp[0]][3] + AP[B_tmp[1]][3])
                    elif len(A_tmp) == 1 and len(B_tmp) == 1:
                        cnt = max(cnt, AP[A_tmp[0]][3])
                else:
                    cnt = max(cnt, AP[A_tmp[0]][3] + AP[B_tmp[0]][3])
            elif A_tmp:
                cnt = max(cnt, AP[A_tmp[0]][3])
            elif B_tmp:
                cnt = max(cnt, AP[B_tmp[0]][3])
        ans += cnt

        if time == M:
            continue

        ax, ay = (ax + dx[A_trail[time]]), (ay + dy[A_trail[time]])
        bx, by = (bx + dx[B_trail[time]]), (by + dy[B_trail[time]])

    print(f'#{tc} {ans}')