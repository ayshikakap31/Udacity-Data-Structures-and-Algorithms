## \## Task0

\*\*Description\*\*: The problem involves to print the first record of texts and the last record of calls.



\*\*Approach\*\*: Extracted using index based element access.



\*\*Complexity Analysis\*\*:

\- \*\*Algorithm\*\*: A constant time access without any iteration.

\- \*\*Big O Notation\*\*: $O(1)$ 

\- \*\*Justification\*\*: It allows direct memory address computation without any iteration.



## \## Task1

\*\*Description\*\*: The problem involves to find different telephone numbers in the records



\*\*Approach\*\*: Extract telephone numbers from both the sender and receiver fields of all text and call records using two separate loops (one iterating over texts and one over calls). Each number is added to a set to ensure uniqueness. Finally, the total count of unique telephone numbers is obtained by printing the length of the set.



\*\*Complexity Analysis\*\*:

\- \*\*Algorithm\*\*: Linear traversal of two lists (texts and calls) with constant-time insertions into a set.

\- \*\*Big O Notation\*\*: $O(n)$, where n = n1+n2 where n1 is the length of calls and n2 is the total length of texts.

\- \*\*Justification\*\*: Each list is iterated exactly once, and each operation inside the loops (indexing and set.add) runs in constant time on average, resulting in linear time complexity proportional to the total number of elements processed.



## \## Task2

\*\*Description\*\*: The problem involves to find which telephone number spent the longest time on the phone during the period.



\*\*Approach\*\*: Each telephone number is mapped to its corresponding call durations using a dictionary. For every call record, the call duration is added to the list associated with both the calling and receiving numbers, allowing multiple call durations per number to be stored. After processing all call records, the total call duration for each telephone number is computed, and the number with the maximum cumulative duration is identified.



\*\*Complexity Analysis\*\*:

\- \*\*Algorithm\*\*: Iterate through all call records to accumulate total call durations for each phone number using a dictionary. Then traverse the dictionary to compute the total duration per number and identify the phone number with the maximum cumulative call duration.

\- \*\*Big O Notation\*\*: $O(n)$, where n is the number of call records.

\- \*\*Justification\*\*: The calls list is traversed once to build the duration mapping and the total duration values are aggregated in linear time.



## \## Task3

\*\*Description\*\*: The problem involves to find all of the area codes and mobile prefixes called by people in Bangalore. Also find what percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore?



\*\*Approach\*\*: All calls originating from fixed-line numbers starting with (080) are considered. For each such call, the receiving number is examined to determine whether it is a fixed line, mobile number, or telemarketer. The corresponding area code or prefix is extracted and stored in a list. This list is then converted into a set and sorted to obtain all unique area codes and mobile prefixes called by people in Bangalore. Finally, the number of calls made to Bangalore fixed-line numbers (080) is counted and used to calculate the percentage of calls from fixed lines in Bangalore that are also made to fixed lines within Bangalore.



\*\*Complexity Analysis\*\*:

\- \*\*Algorithm\*\*: Iterate through all call records to extract the area or service codes of numbers called by Bangalore fixed-line users. Store the extracted codes in a list, compute the unique codes for display, and count the proportion of calls made to Bangalore fixed lines.

\- \*\*Big O Notation\*\*: $O(n)$, where n is the number of call records in calls.

\- \*\*Justification\*\*: Each call record is processed once, and all operations inside the loops: string prefix checks, fixed-length string parsing, list appends, and counting—run in constant time. Creating a set of called codes and counting Bangalore-to-Bangalore calls both take linear time relative to the number of call records, resulting in an overall linear time complexity.



## \## Task4

\*\*Description\*\*: The problem involves to identify numbers that might be doing telephone marketing.



\*\*Approach\*\*: Extract all numbers from which calls were made and to. Then we check whether that number has received any call, text received or sent from it. All such numbers are removed from list of telephone number from which calls were made to get possible telemarketers numbers.



\*\*Complexity Analysis\*\*:

\- \*\*Algorithm\*\*: Traverse all call records to collect unique calling and receiving phone numbers using sets. Eliminate numbers that both make and receive calls, and further remove any numbers that appear in text message records. Finally, sort and display the remaining numbers as potential telemarketers.

\- \*\*Big O Notation\*\*: $O(n+m+nlogn)$, where n is the number of call records, m is the number of text records, and k is the number of remaining candidate phone numbers to be printed.

\- \*\*Justification\*\*: The calls list is traversed once to build the initial sets, and set membership checks and removals are performed in constant time on average. The texts list is then traversed once to remove any numbers that appear in text records. The final sorting step dominates the runtime for the remaining candidates and takes O(k log k) time, resulting in an overall complexity of O(n + m + k log k).



