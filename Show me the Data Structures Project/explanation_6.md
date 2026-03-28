#### Reasoning Behind Decisions:

A singly linked list was used to represent the input structure, while Python sets were used in the union and intersection functions to efficiently handle uniqueness. For union, elements from both linked lists were added to a set so duplicates were removed automatically. For intersection, values from both lists were stored in separate sets and their common elements were found using set intersection. The final results were inserted into a new linked list, and sorted() was used to produce a clean, predictable output order.



#### Time Efficiency:

Building the sets takes linear time in the size of the two linked lists. The union and intersection set operations are also efficient on average. However, creating the final linked list using the current append() method takes extra time because each append traverses to the end of the list. Also, sorting adds additional cost. Overall, if the two lists have sizes n and m, the total time is approximately O(n + m + k log k + k²) in the worst case, where k is the number of elements in the result.



#### Space Efficiency:

Extra space is used for the sets that store elements from the linked lists, and also for the new linked list that stores the result. Therefore, the space complexity is O(n + m) in the worst case, since all unique elements may need to be stored separately.

