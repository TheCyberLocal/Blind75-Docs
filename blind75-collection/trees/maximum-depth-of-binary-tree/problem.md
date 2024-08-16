# Blind75: Maximum Depth of Binary Tree

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**

-   **Input:** `root = [1,2,3,null,null,4]`
-   **Output:** `3`

**Example 2:**

-   **Input:** `root = []`
-   **Output:** `0`

### Constraints

-   `0 <= The number of nodes in the tree <= 100.`
-   `-100 <= Node.val <= 100`

---

### Approach: Recursive Depth Calculation

-   **Time Complexity:** `O(n)`, where `n` is the number of nodes in the tree.
-   **Space Complexity:** `O(h)`, where `h` is the height of the tree, for the recursive call stack.
-   **Description:** This approach calculates the maximum depth of a binary tree using recursion. The depth of the tree is the greater of the depths of the left and right subtrees, plus one for the current node. If a node is `null`, it contributes zero to the depth.
-   **Algorithm:**

    1. Start at the root of the tree.
    2. If the current node is `null`, return `0`.
    3. Recursively calculate the depth of the left subtree.
    4. Recursively calculate the depth of the right subtree.
    5. Return the maximum of the left and right subtree depths, plus `1` for the current node.

```pseudo
function maxDepth(root):
	if not root:
		return 0

	leftDepth = maxDepth(root.left)
	rightDepth = maxDepth(root.right)

	return max(leftDepth, rightDepth) + 1
```
