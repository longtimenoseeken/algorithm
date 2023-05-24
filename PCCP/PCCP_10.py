# PCCP_10 주차요금 정산

f = [180, 5000, 10, 600]
r = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

from collections import defaultdict
import math

def solution(fees, records):
    basic_time = fees[0]
    basic_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    parking_info = defaultdict(str)
    time_info = defaultdict(str)

    for info_item in records:
        time, car_num, info = info_item.split()
        time_info[car_num] = 0
    time_info = dict(sorted(time_info.items()))
    
    for info_item in records:
        time, car_num, info = info_item.split()
        if info == "IN":
            parking_info[car_num] = time
        elif info == "OUT":
            in_hh, in_mm = map(int, parking_info[car_num].split(':'))
            out_hh, out_mm = map(int, time.split(':'))
            parking_mm = (out_hh - in_hh) * 60 + (out_mm - in_mm)
            time_info[car_num] += parking_mm
            parking_info[car_num] = 0

    for car_num in parking_info:
            if parking_info[car_num] != 0:
                in_hh, in_mm = map(int, parking_info[car_num].split(':'))
                out_hh, out_mm = 23, 59
                parking_mm = (out_hh - in_hh) * 60 + (out_mm - in_mm)
                time_info[car_num] += parking_mm

    answer = []

    for car_num in time_info:
        parking_mm = time_info[car_num]
        fee = basic_fee + math.ceil((max(parking_mm, basic_time) - basic_time) / unit_time) * unit_fee
        answer.append(fee)

    return answer

print(solution(f, r))