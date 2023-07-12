# 5176_이진탐색

def tree(idx):
    global cnt

    if idx > N:
        return
    
    tree(idx*2)
    answer_tree[idx] = cnt
    cnt += 1
    tree(idx * 2 + 1)

for tc in range(1, int(input()) + 1):
    N = int(input())

    answer_tree = [0] * (N + 1)
    cnt = 1

    tree(1)

    root = answer_tree[1]
    mid = answer_tree[N//2]
    print(f'#{tc} {root} {mid}')