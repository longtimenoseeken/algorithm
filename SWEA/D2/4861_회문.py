# 4861_회문

def check(matrix):
    global ans
    for r in range(N):
        for i in range(N - M + 1):
            word = matrix[r][i:i + M]
            if word == word[::-1]:
                ans = word
                break

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    words = [input() for _ in range(N)]
    r_words = [''.join(i) for i in zip(*words)]

    ans = ''

    check(words)
    if ans == '':
        check(r_words)

    print(f'#{tc} {ans}')