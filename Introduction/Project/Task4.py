"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
num_calls_from = set()
num_calls_to = set()
for call_info in calls:
  num_calls_from.add(call_info[0])
  num_calls_to.add(call_info[1])
for check in num_calls_to:
  if check in num_calls_from:
    num_calls_from.remove(check)
for text_num in texts:
  if text_num[0] in num_calls_from:
    num_calls_from.remove(text_num[0])
  if text_num[1] in num_calls_from:
    num_calls_from.remove(text_num[1])
print("These numbers could be telemarketers:")
for num in sorted(num_calls_from):
  print(num)