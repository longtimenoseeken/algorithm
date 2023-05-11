from collections import deque

def downstair(row, height):
    cnt = 0
    stair = deque()
    while row or stair:
        cnt += 1
        row_tmp = deque()
        stair_tmp = deque()

        while stair:
            s = deque.popleft(stair)
            if s > 1:
                stair_tmp.append(s-1)
        stair = stair_tmp
        
        while row:
            d = deque.popleft(row)
            if d > 0:
                row_tmp.append(d-1)
            elif d == 0 and len(stair) < 3:
                stair.append(height)
            elif d == 0 and len(stair) >= 3:
                row_tmp.append(d)

        row = row_tmp
    return cnt

for tc in range(1, int(input()) + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    stairs = []
    people = []
    ans = 987654321

    # 계단 좌표 및 계단 높이 저장
    # 사람들 좌표 저장
    for r in range(N):
        for c in range(N):
            if matrix[r][c] > 1:
                stairs.append((r, c, matrix[r][c]))
            elif matrix[r][c] == 1:
                people.append((r, c))

    # 사람별로 각 계단까지 거리 계산
    distance = []
    for person in people:
        distance.append((abs(person[0] - stairs[0][0]) + abs(person[1] - stairs[0][1]), abs(person[0] - stairs[1][0]) + abs(person[1] - stairs[1][1])))
    # 계단별로 각 사람 배분(부분집합)
    for i in range(1 << len(distance)):
        Astair = deque()
        Bstair = deque()
        for j in range(len(distance)):
            if i & (1 << j):
                Astair.append(distance[j][0])
            else:
                Bstair.append(distance[j][1])

        # 각 경우에서 걸리는 시간은 더 오래 걸리는 계단에서의 소요 시간
        # 정답은 경우별 소요 시간 가운데 최소값
        ans = min(ans, max(downstair(Astair, stairs[0][2]), downstair(Bstair, stairs[1][2])))

    print(f'#{tc} {ans}')