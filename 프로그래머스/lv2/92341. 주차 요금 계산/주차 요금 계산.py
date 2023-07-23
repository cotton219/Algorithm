import math
def solution(fees, records):
    car_num = sorted(list(set([i[6:10] for i in records])))

    result = []
    for j in car_num: 
        time = []
        for i in records:
            if (i[6:10] == j):
                time.append(i[0:5])
        if len(time)%2!=0:
            time.append('23:59')

        t = len(time)-1
        total_time = 0
        while t >= 0:
            if t%2==1:
                out_ = time[t]
                in_ = time[t-1]
                total_time += (int(out_[0:2]) - int(in_[0:2]))*60 + int(out_[3:5]) - int(in_[3:5])
            t -= 1
        if total_time <= fees[0]:
            result.append(fees[1])
        else:
            result.append(math.ceil((total_time-fees[0])/fees[2])*fees[3]+fees[1])
    return result