#### Reasoning Behind Decisions:

An OrderedDict was used to efficiently maintain the order of elements based on usage. The key idea of LRU cache is to remove the least recently used item when capacity is exceeded. When a key is accessed via get, it is moved to the end to mark it as recently used. When inserting via set, if the cache is full, the first item (least recently used) is removed. This design avoids manual linked list handling and leverages built-in efficient operations.



#### Time Efficiency:

Both get and set operations run in O(1) average time. Checking key existence, updating values, moving elements to the end, and popping the least recently used item are all constant-time operations due to the underlying hash map and doubly linked list structure of OrderedDict.



#### Space Efficiency:

The space complexity is O(capacity) since the cache stores at most a fixed number of key-value pairs. No additional significant space is used beyond the storage required for the cache itself.

