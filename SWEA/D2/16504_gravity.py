# 16504_gravity

for tc in range(1, int(input()) + 1):
    N = int(input())
    boxes = list(map(int, input().split()))

    ans = 0

    for i in range(N):
        if boxes[i]:
            for j in range(i, N):
                if boxes[j] < boxes[i]:
                    ans += 1
            break

    print(f'#{tc} {ans}')