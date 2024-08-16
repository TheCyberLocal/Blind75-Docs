# Blind75: Invert Binary Tree

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given the root of a binary tree `root`. Invert the binary tree and return its root.

**Example 1:**

-   **Input:** `root = [1,2,3,4,5,6,7]`
-   **Output:** `[1,3,2,7,6,5,4]`

**Example 2:**

-   **Input:** `root = [3,2,1]`
-   **Output:** `[3,1,2]`

**Example 3:**

-   **Input:** `root = []`
-   **Output:** `[]`

### Constraints

-   `0 <= The number of nodes in the tree <= 100`
-   `-100 <= Node.val <= 100`

---

### Approach 1: Recursive Inversion

-   **Time Complexity:** `O(n)` where `n` is the number of nodes in the tree.
-   **Space Complexity:** `O(h)` where `h` is the height of the tree due to the recursion stack.
-   **Description:** The idea is to traverse the tree recursively, and at each node, swap its left and right children. Continue this process for all nodes to achieve a complete inversion of the tree.
-   **Algorithm:**

    1. If the tree is empty (i.e., the root is null), return null.
    2. Recursively invert the left and right subtrees.
    3. Swap the left and right children of the current node.
    4. Return the current node after inverting its subtrees.

```pseudo
function invertTree(root):
	if root is null:
		return null

	leftInverted = invertTree(root.left)
	rightInverted = invertTree(root.right)

	root.left = rightInverted
	root.right = leftInverted

	return root
```
