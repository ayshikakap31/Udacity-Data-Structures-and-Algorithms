#### Reasoning Behind Decisions:

A recursive approach was used to traverse directories because the folder structure can have arbitrary depth. The function checks each entry in the given path: if it is a file, it verifies whether it matches the required suffix; if it is a directory, the function recursively explores it. This ensures all nested subdirectories are searched without needing an explicit stack or queue.



#### Time Efficiency:

In the worst case, every file and directory under the given path is visited exactly once. If there are N total files and directories, the time complexity is O(N). Each file involves a constant-time suffix check, and directory traversal is linear.



#### Space Efficiency:

The space complexity is O(N) for storing the resulting list of matching file paths. Additionally, recursive calls use stack space proportional to the maximum directory depth D, giving O(D) auxiliary space.

