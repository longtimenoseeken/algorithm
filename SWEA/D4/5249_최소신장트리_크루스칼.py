# 5249_최소신장트리_크루스칼

# p라는 보조 리스트 활용
# p의 인덱스(i)는 노드 번호를, p[i]는 해당 노드의 최종 부모 노드를 의미

# 초기 세팅: 자기 자신을 부모로 하는 리스트 만드는 함수
def make_set(x):
    p[x] = x

# 해당 노드의 최종 부모를 찾는 함수
def find_set(x):
    # 자기 자신이 최종 부모가 아니라면,
    if p[x] != x:
        # 계속 거슬러 올라가 최종 부모를 찾아 해당 인덱스에 저장하여 반환
        p[x] = find_set(p[x])
    return p[x]

# 두 노드를 연결하는 함수
def union(x, y):
    # y의 최종 부모 노드는 == x의 최종 부모 노드
    p[find_set(y)] = find_set(x)

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(E)]
    info.sort(key = lambda x: x[2])

    p = [0] * (V + 1)

    for i in range(V + 1):
        make_set(i)

    cnt = 0
    ans = 0

    for x, y, w in info:
        if find_set(x) != find_set(y):
            union(x, y)
            ans += w
            cnt += 1
        if cnt == V:
            break

    print(f'#{tc} {ans}')