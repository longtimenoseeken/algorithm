for _ in range(10):
    tc = int(input())
    N = 100
    arr = [list(map(int, input())) for _ in range(N)]
    #시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]
            if arr[i][j] == 3:
                end = [i, j]

    stack = [start]  # [1, 1]
    visited = []
    answer = 0
    while stack:
        current = stack.pop()
        visited.append(current)

        r = current[0]
        c = current[1]

        direction_list = [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]
        for dir in direction_list: #4방탐색
            r_1 = dir[0]
            r_2 = dir[1]

            if r_1 < 0 or r_1 >= N or r_2 < 0 or r_2 >= N:
                continue

            if dir == end:
                answer = 1

            if arr[r_1][r_2] == 0 and dir not in visited:
                stack.append(dir)




    print(f'#{tc} {answer}')