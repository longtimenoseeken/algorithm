# 미생물 격리

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
rev = [0, 2, 1, 4, 3]


for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    germ = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        check = dict()
        for i in range(K):
            r, c, n, d = germ[i]
            if not n:
                continue
            nr, nc = r + dr[d], c + dc[d]
            germ[i][0], germ[i][1] = nr, nc

            if nr in [0, N-1] or nc in [0, N-1]:
                n //= 2
                d = rev[d]
            
            if (nr, nc) not in check.keys():
                check[(nr, nc)] = [(i, n, d)]
            else:
                check[(nr, nc)].append((i, n, d))

        for j in check.values():
            if len(j) == 1:
                i, n, d = j[0]
                germ[i][2] = n
                germ[i][3] = d

            elif len(j) > 1:
                cnt = 0
                ni, nn = -1, -1
                for i, n, d in j:
                    cnt += n
                    if n > nn:
                        ni = i
                        nn = n
                germ[ni][2] = cnt

                for i, n, d in j:
                    if i != ni:
                        germ[i][2] = 0

    ans = 0
    for r, c, n, d in germ:
        ans += n
    
    print(f'#{tc} {ans}')