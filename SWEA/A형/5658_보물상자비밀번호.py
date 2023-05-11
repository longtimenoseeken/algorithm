# 보물상자 비밀번호

base = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

def trans(num):
    cnt = 0
    n = len(num)
    for i in range(n):
        cnt += (base.get(num[i]) * (16 ** (n - i - 1)))
    return cnt

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    pw = input()
    pw_list = []

    for _ in range(N//4):
        for i in range(4):
            x = trans(pw[i*(N//4):(i+1)*(N//4)])
            if x not in pw_list:
                pw_list.append(x)
        pw = pw[1:] + pw[0]

    pw_list.sort(key=lambda x: -x)

    ans = pw_list[K-1]

    print(f'#{tc} {ans}')