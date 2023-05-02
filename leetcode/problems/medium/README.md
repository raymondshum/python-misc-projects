# Leetcode DocStrings

This README file was autogenerated with readme_generator.py.

# Contents
- [1004_max_consecutive_ones_iii](#1004_max_consecutive_ones_iiipy)
- [1448_count_good_nodes_in_binary_tree](#1448_count_good_nodes_in_binary_treepy)

# 1004_max_consecutive_ones_iii.py

**File Name**: 1004_max_consecutive_ones_iii.py

**Key Point**:  Sliding window. Window size is determined by "k" allowed flipped zeros. 

**Link**: [max consecutive ones iii](https://leetcode.com/problems/max-consecutive-ones-iii/ )

**Method**: Increase window until max number of flipped zeroes is exceeded. Retract window from the left until number of flipped zeroes equals max. Increase window size and repeat until no numbers remain. 

**Returns**: Max number of consecutive 1's in the list.


[Return to Top](#contents)

---

# 1448_count_good_nodes_in_binary_tree.py

**File Name**: 1448_count_good_nodes_in_binary_tree.py

**Key Point**:  Track the current max node value. Update the answer at every node (whether condition is met). 

**Link**: [count good nodes in binary tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/ )

**Method**: Using DFS, traverse the tree. At each node, track the maximum node value encountered so far. Iterate answer if "good node" condition is met. Call method recursively for left and right subtrees. Return accumulated answer. 

**Returns**: Number of "good" nodes in the binary tree. A node is "good" if there are no nodes between it and the root with a greater value. The root is always a good node.


[Return to Top](#contents)

---
