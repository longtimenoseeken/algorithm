# 활주로 건설

# row별 체크 함수
def check(row):
    cnt = 1
    # 두번째 칸부터 시작해서 앞칸 검토
    for i in range(1, N):
        # 높이가 그대로인 경우: cnt 1추가
        if row[i] - row[i-1] == 0:
            cnt += 1
        # 높이가 1 높아지는 경우 & cnt가 X만큼 쌓인 경우: 설치 가능(cnt 초기화)
        elif row[i] - row[i-1] == 1 and cnt >= X:
            cnt = 1
        # 높이가 1 낮아지는 경우 & cnt가 0보다 크거나 같은 경우: 설치 가능(설치하고 cnt = 1-X로 하여 다음 높이 변화 또는 마지막까지 cnt가 제대로 쌓이는지 검토)
        elif row[i] - row[i-1] == -1 and cnt >= 0:
            cnt = 1-X
        # 그 외 모든 경우는 설치 불가능: 바로 0으로 return
        else:
            return 0
    # 마지막까지 검토했을 때 cnt가 0보다 크면 통과(1로 return)
    if cnt >= 0:
        return 1
    # 아니라면 0으로 return
    else:
        return 0


for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    reverse = list(map(list, zip(*matrix)))
    ans = 0

    for i in range(N):
        ans += (check(matrix[i]) + check(reverse[i]))

    print(f'#{tc} {ans}')