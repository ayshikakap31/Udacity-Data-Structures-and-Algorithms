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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_telephone_nos = set()
for text_nos in texts:
  unique_telephone_nos.add(text_nos[0])
  unique_telephone_nos.add(text_nos[1])
for call_nos in calls:
  unique_telephone_nos.add(call_nos[0])
  unique_telephone_nos.add(call_nos[1])
print(f"There are {len(unique_telephone_nos)} different telephone numbers in the records.")