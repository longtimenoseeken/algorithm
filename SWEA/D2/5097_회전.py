# 5097_회전

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    num_seq = list(input().split())
    
    ans = num_seq[M % N]

    print(f'#{tc} {ans}')