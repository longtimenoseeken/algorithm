for tc in range(1, int(input()) + 1):
    D, M, MM, Y = map(int, input().split())
    plan = list(map(int, input().split()))
    cum_sum = [0 for _ in range(12)]
    cum_sum[0] = min(plan[0] * D, M)

    for i in range(1, 12):
        cum_sum[i] = min(plan[i] * D, M) + cum_sum[i-1]
        if i >= 2:
            cum_sum[i] = min(cum_sum[i], MM + cum_sum[i-3])
        print(cum_sum)
    
    ans = min(cum_sum[11], Y)

    print(f'#{tc} {ans}')