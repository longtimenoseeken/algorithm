# PCCP_1_외톨이알파벳

sample = "edeaaabbccd"

def solution(input_string):
    N = len(input_string)
    tmp = set()

    visited = set(input_string[0])

    for i in range(1, N):
        if input_string[i] == input_string[i - 1]:
            continue

        if input_string[i] in visited:
            tmp.add(input_string[i])
        
        visited.add(input_string[i])

    if not tmp:
        ans = 'N'
        return ans

    ans = ''
    for c in sorted(tmp):
        ans += c

    return ans

print(solution(sample))