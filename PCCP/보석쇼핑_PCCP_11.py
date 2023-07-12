# PCCP_11_보석쇼핑_시간초과

sample = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	

from collections import defaultdict

def solution(gems):
    gems_kind = set(gems)                       #보석 종류

    gems_cnt = defaultdict(int)                 # 구간 내 보석별 숫자 기록할 dict
    
    L = R = 0                                   # 포인터
    min_length = 987654321                      # 최소값 갱신 위한 임의값
    
    while R < len(gems):                        # R 포인터가 범위 내에 있는 동안
        gems_cnt[gems[R]] += 1                  # R 포인터가 가리키는 보석 입력
        R += 1                                  # R 포인터 이동

        if len(gems_cnt) == len(gems_kind):     # 모든 보석이 기록되는 순간
            while L < R:                        # L 포인터 이동, 단 R보다 작은 범위에서
                if gems_cnt[gems[L]] > 1:       # L 포인터가 가리키는 보석을 빼도 되면
                    gems_cnt[gems[L]] -= 1      # 빼고
                    L += 1                      # L 포인터 이동
                elif R - L < min_length:        # 뺄 수 없고 최소값 갱신이 가능하다면
                    min_length = R - L          # 최소값을 갱신하고
                    ans = [L + 1, R]            # 정답도 갱신
                    break                       # break하고 R 포인터로 다시 이동
                else:                           # 뺄 수 없지만 최소값 갱신 안되면
                    break                       # 그냥 break하고 R 포인터로 다시 이동

    return ans

print(solution(sample))