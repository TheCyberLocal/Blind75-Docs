# Blind75: Binary Tree Maximum Path Sum

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node cannot appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

**Example 1:**

- **Input:** `root = [1,2,3]`
- **Output:** `6`
- **Explanation:** The path is `2 -> 1 -> 3` with a sum of `2 + 1 + 3 = 6`.

**Example 2:**

- **Input:** `root = [-15,10,20,null,null,15,5,-5]`
- **Output:** `40`
- **Explanation:** The path is `15 -> 20 -> 5` with a sum of `15 + 20 + 5 = 40`.

### Constraints

- `1 <= The number of nodes in the tree <= 1000`
- `-1000 <= Node.val <= 1000`

---

### Approach 1: Depth-First Search (DFS) with Backtracking

- **Time Complexity:** `O(n)` where `n` is the number of nodes in the tree.
- **Space Complexity:** `O(h)` where `h` is the height of the tree, which is the maximum depth of the recursion stack.
- **Description:** This approach uses Depth-First Search (DFS) to explore all paths from each node. The algorithm calculates the maximum path sum that includes the node and returns the maximum sum of paths that can be extended to its parent node. At each node, the algorithm updates the global maximum path sum if the sum of the paths from the left and right children through the node is greater than the current maximum.
- **Algorithm:**

  1. Define a helper function `max_path_sum_from_node(node)` that returns the maximum path sum that can be extended to the node's parent.
  2. For each node, recursively calculate the maximum path sum from its left and right children.
  3. Update the global maximum path sum if the sum of the current node's value and the maximum path sums from its left and right children is greater than the current global maximum.
  4. Return the maximum path sum that can be extended to the node's parent, which is the node's value plus the maximum of the path sums from its left and right children.
  5. The result is stored in the global maximum path sum after exploring all nodes.

```python
def max_path_sum(root: Optional[TreeNode]) -> int:
	max_sum = float('-inf')

	def max_path_sum_from_node(node: int) -> int:
		if not node:
			return 0

		left_sum = max(max_path_sum_from_node(node.left), 0)
		right_sum = max(max_path_sum_from_node(node.right), 0)

		local_max = node.val + left_sum + right_sum
		max_sum = max(max_sum, local_max)

		return node.val + max(left_sum, right_sum)

	max_path_sum_from_node(root)
	return max_sum
```
