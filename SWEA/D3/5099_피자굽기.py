# 5099_피자굽기

from collections import deque

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    fire = deque()
    cnt = 0

    for i in range(N):
        cnt += 1
        fire.append((cnt, pizza.pop(0)))

    while fire:
        num, cheeze = fire.popleft()
        ans = num
        cheeze //= 2
        if cheeze != 0:
            fire.append((num, cheeze))
        elif cnt < M:
            cnt += 1
            fire.append((cnt, pizza.pop(0)))

    print(f'#{tc} {ans}')