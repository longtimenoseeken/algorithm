# 5177_이진힙

def heap_push(item):
    heap.append(item)

    child = len(heap) - 1
    parent = child // 2

    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2

for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    heap = ['최소힙: ']

    for num in nums:
        heap_push(num)

    ans = 0

    while N != 1:
        ans += heap[N // 2]
        N = N // 2

    print(f'#{tc} {ans}')