# 원자소멸 시뮬레이션

from collections import defaultdict, deque


dx = [0, 0, -1/2, 1/2]
dy = [1/2, -1/2, 0, 0]

for tc in range(1, int(input()) + 1):
    N = int(input())
    atoms = deque()
    ans = 0

    for _ in range(N):
        x, y, d, k = map(int, input().split())
        atoms.append((x, y, d, k))

    while atoms:
        tmp = defaultdict(list)
        for _ in range(len(atoms)):
            x, y, d, k = deque.popleft(atoms)
            nx, ny = x + dx[d], y + dy[d]

            if -1000 <= nx <= 1000 and -1000 <= ny <= 1000:
                tmp[(nx, ny)].append((nx, ny, d, k))

        for atom in tmp.values():
            if len(atom) == 1:
                atoms.append((atom[0]))
            elif len(atom) > 1:
                for energy in atom:
                    ans += energy[3]

    print(f'#{tc} {ans}')