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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
nos_called = []
for call_info in calls:
  if call_info[0].startswith("(080)"):
    if call_info[1].startswith("(0"):
      start_index = 0
      end_index = 0
      for index, num in enumerate(call_info[1]):
        if num == "(":
          start_index = index+1
        if num == ")":
          end_index = index
      nos_called.append(call_info[1][start_index:end_index])
      # if call_info[1].startswith("(080)"):
      #   count += 1
    elif call_info[1].startswith("140"):
      nos_called.append('140')
    else:
      nos_called.append(call_info[1][:4])
print("The numbers called by people in Bangalore have codes:")
for code in sorted(set(nos_called)):
  print(code)
count = 0
for call_to in nos_called:
  if call_to == '080':
    count += 1
per_count = (count/len(nos_called))*100
print(f"{per_count:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
