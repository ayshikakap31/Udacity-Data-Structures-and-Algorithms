#### Reasoning Behind Decisions:

Huffman coding was implemented using a greedy approach with a min-heap to always combine the two least frequent characters. A HuffmanNode class represents tree nodes, and the \_\_lt\_\_ method enables heap comparisons. Frequencies are computed using a dictionary, and the Huffman tree is built iteratively. Codes are generated via recursive traversal, assigning '0' for left and '1' for right. Special handling was added for edge cases like empty input and single-character input to ensure correctness. Encoding replaces characters with their codes, and decoding traverses the tree based on bits.



#### Time Efficiency:

Building the frequency map takes O(n) time. Constructing the Huffman tree using a heap takes O(k log k), where k is the number of unique characters. Generating codes requires traversing the tree, which is O(k). Encoding the string takes O(n), and decoding also takes O(n). Overall, the time complexity is O(n + k log k).



#### Space Efficiency:

The space complexity is O(n + k). The frequency map and encoded output require space proportional to input size n, while the Huffman tree and code dictionary require space proportional to the number of unique characters k. Additional recursive stack space is O(h), where h is the height of the tree (at most k).

