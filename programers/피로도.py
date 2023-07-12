# 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

k = 80
dungeons = [[80,20],[50,40],[30,10]]

from itertools import permutations

def solution(k, dungeons):
    num = len(dungeons)
    perm = permutations(dungeons, num)
    ans = 0

    for case in perm:
        cnt = 0
        energy = k
        for dun in case:
            if energy >= dun[0]:
                cnt += 1
                energy -= dun[1]
                ans = max(ans, cnt)

    return ans

print(solution(k, dungeons))