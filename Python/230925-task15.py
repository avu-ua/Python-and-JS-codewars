# Find the odd int
# https://www.codewars.com/kata/54da5a58ea159efa38000836

# ---------------- Slava --------------------------
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2 != 0][0]


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