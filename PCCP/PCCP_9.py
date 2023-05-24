# PCCP_9 신고결과 받기

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

def solution(id_list, report, k):

    report = list(set(report))
    num = len(id_list)

    user_relation = [[0] * num for i in range(num)]

    for i in range(len(report)):
        reporter, reported = report[i].split()
        user_relation[id_list.index(reporter)][id_list.index(reported)] = 1

    answer = [0] * num

    for c in range(num):
        cnt = 0
        for r in range(num):
            cnt += user_relation[r][c]
            if cnt >= k:
                for r in range(num):
                    answer[r] += user_relation[r][c]
                break

    return answer

print(solution(id_list, report, k))