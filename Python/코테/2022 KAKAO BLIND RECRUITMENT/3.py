def solution(fees, records):
    answer = []
    cars_record = {}
    car_list = []
    cars_time = {}
    for i in records:
        time, car, r = i.split()
        if r == "IN":
            if not car in car_list:
                car_list.append(car)
            mi, se = time.split(":")
            cars_record[car] = int(mi) * 60 + int(se)
        elif r == "OUT":
            t = cars_record[car]
            mi, se = time.split(":")
            e = int(mi) * 60 + int(se)
            if car in cars_time:
                cars_time[car] += e - t
            else:
                cars_time[car] = e - t
            cars_record[car] = -1
    for car in cars_record:
        if cars_record[car] != -1:
            e = 23 * 60 + 59
            t = cars_record[car]
            if car in cars_time:
                cars_time[car] += e - t
            else:
                cars_time[car] = e - t
    
    car_list.sort()
    print(cars_time)
    for car in car_list:
        if cars_time[car] <= fees[0]:
            answer.append(fees[1])
        else:
            left_time = cars_time[car] - fees[0]
            if (left_time / fees[2]) > (left_time // fees[2]):
                count = (left_time//fees[2]) + 1
            else:
                count = (left_time//fees[2])
            answer.append(fees[1] + count * fees[3])
            
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
# 05:34 5961 IN
# 06:34 0000 OUT
# 07:59 5961 OUT
# 07:59 0148 IN
# 18:59 0000 IN
# 19:09 0148 OUT
# 22:59 5961 IN
# 23:00 5961 OUT