# PCCP_2_체육대회

sample = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]

from itertools import permutations, combinations

def solution(ability):
    R = len(ability)
    C = len(ability[0])
    ans = 0

    for people in combinations(range(R), C):
        for order in permutations(range(C), C):
            cnt = 0
            for i in range(C):
                cnt += ability[people[i]][order[i]]
            ans = max(ans, cnt)

    return ans

print(solution(sample))