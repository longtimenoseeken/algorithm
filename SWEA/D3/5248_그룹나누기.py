# 5248_그룹나누기

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    vote = list(map(int, input().split()))

    p = [0] * (N+1)
    for i in range(N+1):
        make_set(i)

    for i in range(M):
        if find_set(vote[2*i]) != find_set(vote[2*i + 1]):
            union(vote[2*i], vote[2*i+1])

    ans_set = set()

    for i in range(1, N+1):
        ans_set.add(find_set(i))

    ans = len(ans_set)

    print(f'#{tc} {ans}')