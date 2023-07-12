# PCCP_10 주차요금 정산

f = [180, 5000, 10, 600]
r = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

from collections import defaultdict
import math

def solution(fees, records):
    # 요금 정보 기록(기본 시간, 기본 요금, 단위 시간, 단위 요금)
    basic_time = fees[0]
    basic_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    # 중간 연산을 위해 중간중간 주차 정보를 기록할 딕셔너리
    parking_info = defaultdict(str)
    # 최종 주차 시간이 기록될 딕셔너리
    time_info = defaultdict(str)

    # 주어진 정보 묶음을 풀어 time 딕셔너리에 car_num을 key값, 0을 value값으로 저장
    for info_item in records:
        time, car_num, info = info_item.split()
        time_info[car_num] = 0
    # 차량 번호 오름차순으로 정렬
    time_info = dict(sorted(time_info.items()))
    
    for info_item in records:
        time, car_num, info = info_item.split()
        # 입차 차량의 경우 parking 딕셔너리에 car_num을 key값, 입차 시간을 value값으로 저장
        if info == "IN":
            parking_info[car_num] = time
        # 출차 차량의 경우
        elif info == "OUT":
            # 출차 시간에서 입차 시간을 빼서 분 단위로 계산하여
            in_hh, in_mm = map(int, parking_info[car_num].split(':'))
            out_hh, out_mm = map(int, time.split(':'))
            parking_mm = (out_hh - in_hh) * 60 + (out_mm - in_mm)
            # time 딕셔너리에 저장
            time_info[car_num] += parking_mm
            # parking 딕셔너리는 비우기
            parking_info[car_num] = 0

    # 출차하지 않은 차량 계산(parking 딕셔너리가 비워지지 않은 차량)
    for car_num in parking_info:
        if parking_info[car_num] != 0:
            # 출차 시간을 23:59으로 설정하고 계산
            in_hh, in_mm = map(int, parking_info[car_num].split(':'))
            out_hh, out_mm = 23, 59
            parking_mm = (out_hh - in_hh) * 60 + (out_mm - in_mm)
            time_info[car_num] += parking_mm

    # 주차요금을 계산하여 담을 빈 리스트 제작
    answer = []

    # 차량별 주차 시간에 따라 주차요금 계산하여 answer 리스트에 append
    for car_num in time_info:
        parking_mm = time_info[car_num]
        # 요금 계산식: 기본 요금 + (초과시간/단위시간)(올림)*단위요금
        # 주차 시간이 기본 시간보다 적은 경우 기본 요금으로 계산
        fee = basic_fee + math.ceil((max(parking_mm, basic_time) - basic_time) / unit_time) * unit_fee
        answer.append(fee)

    return answer

print(solution(f, r))