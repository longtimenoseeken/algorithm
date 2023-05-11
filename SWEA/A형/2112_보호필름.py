# 보호필름

from itertools import combinations, product

def check(matrix):
    for c in range(W):
        tmp = 1
        for r in range(1, D):
            if matrix[r][c] == matrix[r-1][c]:
                tmp += 1
            else:
                tmp = 1
            if tmp >= K:
                break
        else:
            return 0
    return 1

def trans(n):
    obj = list(combinations([i for i in range(D)], n))
    for trans_row in obj:
        arr = [x[:] for x in film]
        for drug in product([0, 1], repeat = n):
            for i in range(n):
                arr[trans_row[i]] = [drug[i]] * W

            if check(arr) == 1:
                return 1
    else:
        return 0

for tc in range(1, int(input()) + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    for i in range(K+1):
        if trans(i) == 1:
            ans = i
            break

    print(f'#{tc} {ans}')