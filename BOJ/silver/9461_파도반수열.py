# 9461_파도반수열

for tc in range(1, int(input()) + 1):
    N = int(input())

    dp = [0, 1, 1, 1, 2, 2]

    for i in range(6, N + 1):
        dp.append(dp[i - 1] + dp[i - 5])

    print(dp[N])