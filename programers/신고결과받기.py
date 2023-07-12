# 신고결과받기

def solution(id_list, report, k):

    # 중복 신고 제거
    report = list(set(report))
    # 총 유저 숫자
    num = len(id_list)

    # 유저 관계 받을 빈 행렬 제작
    user_relation = [[0] * num for _ in range(num)]

    # 행이 신고자, 열이 피신고자, user_relation[reporter][reported]에 기록
    for i in range(len(report)):
        reporter, reported = report[i].split()
        user_relation[id_list.index(reporter)][id_list.index(reported)] = 1

    # 신고 횟수 받을 빈 리스트 제작
    answer = [0] * num

    # 피신고 횟수를 셀 것이므로 열 우선 순회
    for c in range(num):
        # 피신고 횟수를 셀 cnt 변수
        cnt = 0
        # 피신고 횟수를 세며
        for r in range(num):
            cnt += user_relation[r][c]
            # k보다 같거나 커지는 경우에만
            if cnt >= k:
                # answer 리스트에 그 사람을 신고한 기록 추가하고 break(그 이후에는 셀 필요 없음)
                for r in range(num):
                    answer[r] += user_relation[r][c]
                break

    return answer