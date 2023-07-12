# 5208_전기버스2

# N번 정류장에서 1번 정류장으로 돌아가면서 가장 멀리 갈 수 있는 정거장을 찾습니다.
def which_stop_farthest(current):
    global ans
    # 첫 번째 정류장에 도착하면 return(첫 번째 정류장 충전은 횟수로 치지 않으므로 -1)
    if current == 0:
        ans -= 1
        return

    ans += 1

    check = []
    # 현재 위치부터 뒤로 탐색하여 현재 위치까지 올 수 있는 정류장 찾기
    for back in range(current - 1, -1, -1):
        if (current - back) <= battery[back]:
            check.append(back)

    # 해당 정류장 가운데 가장 앞에 있는 정류장 찾아서 그 곳을 current로 하여 재귀
    next_current = min(check)
    which_stop_farthest(next_current)

for tc in range(1, int(input())+1):
    battery = list(map(int, input().split()))
    goal = battery.pop(0)

    ans = 0
    which_stop_farthest(goal - 1)

    print(f'#{tc} {ans}')