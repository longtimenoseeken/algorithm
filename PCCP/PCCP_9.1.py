# PCCP_9 신고결과 받기

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

from collections import defaultdict

def solution(id_list, report, k):
    report = list(set(report))

    report_counting = defaultdict(str)
    for id in id_list:
        report_counting[id] = defaultdict(str)
    for report_item in report:
        reporter, reported = report_item.split()
        report_counting[reported][reporter] = 1

    mail_counting = defaultdict(str)
    for id in id_list:
        mail_counting[id] = 0

    for each_id in report_counting:
        if len(report_counting[each_id]) >= k:
            for key in report_counting[each_id].keys():
                mail_counting[key] += 1

    answer = list(mail_counting.values)
    return answer

print(solution(id_list, report, k))