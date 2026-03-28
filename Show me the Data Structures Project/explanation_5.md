#### Reasoning Behind Decisions:

A blockchain was implemented as a list of Block objects, where each block stores its own data, timestamp, and the hash of the previous block. The calc\_hash() method uses SHA-256 to ensure data integrity by generating a unique hash based on block contents. A genesis block is created during initialization to serve as the starting point of the chain. Each new block links to the previous one via its hash, maintaining the core blockchain property of immutability and traceability.



#### Time Efficiency:

Adding a block is efficient since it only requires accessing the last block and computing a hash, resulting in O(1) time complexity per insertion. Hash computation itself is constant time relative to input size (small fixed data). Printing the blockchain requires traversing all blocks, which takes O(n) time.



#### Space Efficiency:

The blockchain stores all blocks sequentially in a list, so space grows linearly with the number of blocks, resulting in O(n) space complexity. Each block stores fixed-size metadata (timestamp, hashes, and data), so no additional significant overhead is introduced beyond the stored data itself.

