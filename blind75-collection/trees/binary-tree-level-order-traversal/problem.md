# Blind75: Binary Tree Level Order Traversal

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a binary tree `root`, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

**Example 1:**

- **Input:** `root = [1,2,3,4,5,6,7]`
- **Output:** `[[1],[2,3],[4,5,6,7]]`

**Example 2:**

- **Input:** `root = [1]`
- **Output:** `[[1]]`

**Example 3:**

- **Input:** `root = []`
- **Output:** `[]`

### Constraints

- `0 <= The number of nodes in the tree <= 1000`
- `-1000 <= Node.val <= 1000`

---

### Approach 1: Breadth-First Search (BFS)

- **Time Complexity:** `O(n)` where `n` is the number of nodes in the tree.
- **Space Complexity:** `O(n)` for storing the output list and the queue used in the BFS.
- **Description:** This approach uses Breadth-First Search (BFS) to traverse the tree level by level. A queue is used to keep track of the nodes at the current level, and for each node, its children are added to the queue for the next level. The values of nodes at each level are collected into sublists, which are appended to the final output list.
- **Algorithm:**

  1. If the tree is empty, return an empty list.
  2. Initialize a queue with the root node and an empty list to store the result.
  3. While the queue is not empty:
     - Create an empty list for the current level.
     - For each node in the queue:
       - Dequeue the node and add its value to the current level list.
       - Enqueue the node's left and right children if they exist.
     - Append the current level list to the result.
  4. Return the result list containing all levels.

```python
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
	if not root:
		return []

	queue = [root]
	result = []

	while queue:
		level = []

		for _ in range(len(queue)):
			node = queue.pop(0)
			level.append(node.val)

			if node.left:
				queue.append(node.left)

			if node.right:
				queue.append(node.right)

		result.append(level)

	return result
```
