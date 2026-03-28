#### Reasoning Behind Decisions:

A hierarchical structure was modeled using a Group class, where each group can contain users and nested sub-groups. To check membership, an iterative depth-first search (DFS) approach using a stack was chosen instead of recursion to avoid potential recursion depth issues. This ensures that all nested sub-groups are explored efficiently while checking whether a user exists at any level in the hierarchy.



#### Time Efficiency:

In the worst case, all groups and users may need to be explored. If there are G groups and U total users, the time complexity is approximately O(G + U). Each group is visited once, and user lookup within a group is linear in the number of users in that group.



#### Space Efficiency:

The space complexity is O(G) due to the stack used for traversal in the worst case, where all groups may be stored in the stack during the search. No additional significant space is used beyond this auxiliary data structure.

