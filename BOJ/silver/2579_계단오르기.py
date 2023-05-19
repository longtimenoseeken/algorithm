# 2579_계단오르기.py

def check(i, cnt):
    global ans
    print(i)

    if i > N - 1:
        return

    if i == N - 1:
        cnt += stairs[i]
        ans = max(ans, cnt)
        return

    check(i + 1, cnt + stairs[i])

    check(i + 2, cnt + stairs[i])    

N = int(input())

stairs = []

for _ in range(N):
    stairs.append(int(input()))

print(stairs)

ans = 0
visited = []
check(0, 0)

print(ans)