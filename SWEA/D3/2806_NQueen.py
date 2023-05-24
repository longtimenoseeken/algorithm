# 2806_NQueen

def queen(current_depth):
    global ans

    if current_depth == N:
        ans += 1
        return
    
    for i in range(N):
        arr[current_depth] = i
        for check_depth in range(current_depth):
            if arr[check_depth] == i:
                break
            if (current_depth - check_depth) == abs(arr[current_depth] - arr[check_depth]):
                break
        else:
            queen(current_depth + 1)

for tc in range(1, int(input()) + 1):
    N = int(input())

    arr = [0] * N
    ans = 0

    queen(0)

    print(f'#{tc} {ans}')