"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
duration = {}
#map each mobile numbers call duration, add it and then find maximum duration.
for call_info in calls:
  if call_info[0] not in duration:
    duration[call_info[0]] = [int(call_info[3])]
  else:
    duration[call_info[0]].append(int(call_info[3]))
  if call_info[1] not in duration:
    duration[call_info[1]] = [int(call_info[3])]
  else:
    duration[call_info[1]].append(int(call_info[3]))

max_duration = 0
max_duration_mobile = ""
for key, value in duration.items():
  duration[key] = sum(value)
  if duration[key] > max_duration:
    max_duration = duration[key]
    max_duration_mobile = key

print(f"{max_duration_mobile} spent the longest time, {max_duration} seconds, on the phone during September 2016.")