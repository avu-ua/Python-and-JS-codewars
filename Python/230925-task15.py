# Find the odd int
# https://www.codewars.com/kata/54da5a58ea159efa38000836

# ---------------- Slava --------------------------
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2 != 0][0]

# ---------------- Olesia --------------------------
def find_it(seq):
    seq_dict = {}
    for i in seq:
        seq_dict[i] = seq.count(i)
        if seq_dict[i] % 2 == 1:
            return i
        
# ------------------------ Mariia ------------------------
def find_it(seq):
    numbers = tuple(seq)
    for x in numbers:
        if seq.count(x) % 2 == 1:
            return x

        
def find_it(seq):
    return [x for x in tuple(seq) if seq.count(x)%2 == 1][0]

# Simple time difference
# https://www.codewars.com/kata/5b76a34ff71e5de9db0000f2

# ---------------- Slava --------------------------
from datetime import datetime
def solve(arr):
    sorted_times = [datetime.strptime(x, "%H:%M") for x in sorted(arr)]
    time_differences = [(sorted_times[x+1] - sorted_times[x]).total_seconds() - 60 if x < len(sorted_times) - 1 else 24*60*60 - (sorted_times[len(sorted_times) - 1] - sorted_times[0]).total_seconds() - 60 for x, y in enumerate(sorted_times)]
    max_hours = str(int(max(time_differences) // 3600)) if max(time_differences) // 3600 > 9 else "0" + str(int(max(time_differences) // 3600))
    max_minutes = str(int((max(time_differences) - int(max_hours) * 3600) / 60)) if (max(time_differences) - int(max_hours) * 3600) / 60 > 9 else "0" + str(int((max(time_differences) - int(max_hours) * 3600) / 60))
    return max_hours + ":" + max_minutes

# ------------------------ Mariia ------------------------
def solve(alarms):
    if len(alarms) == 1:
        return "23:59"
    else:
        alarms_sorted = sorted(list(map(lambda x: x.split(":"), alarms)))
        minutes = [int(x[0])*60+int(x[1]) for x in alarms_sorted]
        bigger_interval = 1440 - minutes[-1] + minutes[0]
        counter = 1
        for x in minutes:
            if counter < len(minutes):
                interval = minutes[counter] - x
                if interval > bigger_interval:
                    bigger_interval = interval
            counter += 1
            
        hours = str(bigger_interval // 60)
        min = str(bigger_interval % 60 - 1)
        if len(hours) == 1:
            hours = "0" + hours
        if len(min) == 1:
            min = "0" + min
            
        return hours +":"+ min

# ---------------- Olesia --------------------------

def solve(arr):
    unique_set = set(arr)
    arr = list(unique_set)

    if len(arr) == 1:
        return "23:59"
    m_time = []
    m_delta =[]

    for i in arr:
        h, m = list(map(int, i.split(":")))
        mm = h * 60 + m
        m_time.append(mm)
        m_time.sort()

    for x in range(1, len(m_time)):
        prev = m_time[x - 1]
        current = m_time[x]
        delta = current - prev
        m_delta.append(delta)
    if (24 * 60 - m_time[-1] + m_time[0]) > delta:
        aa = 24 * 60 - m_time[-1] + m_time[0]
        m_delta.append(aa)
    max_delta = max(m_delta)-1
    max_h = int(max_delta / 60)
    max_m = int(round((max_delta % 60), 0))
    max_h_str = str(max_h).zfill(2)
    max_m_str = str(max_m).zfill(2)
    return max_h_str+ ":" + max_m_str

time_list = ["21:14", "15:34", "14:51", "06:25", "15:30"]

print(solve(time_list))