# 5189_전자카트

def search(current, distance):
    global min_distance

	# 백트래킹: 검토중인 거리가 현재 최소거리보다 길다면 더이상 검토하지 않습니다.
    if distance < min_distance:
		# 모두 검토했다면 최소거리 갱신
        if len(visited) == N:
            min_distance = min(min_distance, distance + matrix[current][0])
            return

		# 다음 위치 탐색
        for next in range(1, N):
			# 다음 위치 조건: 현재 위치가 아닐 것 & 이미 방문한 곳이 아닐 것
            if current != next and next not in visited:
				# 방문지에 넣고 재귀, 나오면서 pop
                visited.append(next)
                search(next, distance + matrix[current][next])
                visited.pop()

for tc in range(1, int(input()) + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

	# 임의의 최소거리 설정
    min_distance = 10*10*100

	# 0에서 시작하여 모든 경우의 수 탐색
    for i in range(1, N):
        visited = [0, i]

        search(i, matrix[0][i])
    
    print(f'#{tc} {min_distance}')