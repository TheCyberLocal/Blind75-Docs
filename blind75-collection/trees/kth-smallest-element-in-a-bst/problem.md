# Blind75: Kth Smallest Element in BST

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given the root of a binary search tree (BST) and an integer `k`, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

-   The left subtree of every node contains only nodes with keys less than the node's key.
-   The right subtree of every node contains only nodes with keys greater than the node's key.
-   Both the left and right subtrees are also binary search trees.

**Example 1:**

-   **Input:** `root = [2,1,3], k = 1`
-   **Output:** `1`

**Example 2:**

-   **Input:** `root = [4,3,5,2,null], k = 4`
-   **Output:** `5`

### Constraints

-   `1 <= k <= The number of nodes in the tree <= 1000`
-   `0 <= Node.val <= 1000`

---

### Approach 1: Inorder Traversal

-   **Time Complexity:** `O(n)` where `n` is the number of nodes in the tree.
-   **Space Complexity:** `O(h)` where `h` is the height of the tree due to the recursion stack.
-   **Description:** To find the k-th smallest element in the binary search tree, an inorder traversal is performed. This type of traversal visits nodes in increasing order of their values. By keeping a count of the visited nodes, we can identify the k-th node in this sequence, which corresponds to the k-th smallest element in the tree.
-   **Algorithm:**

    1. Initialize a counter to keep track of the number of nodes visited during the traversal.
    2. Define a helper function that performs the inorder traversal:
        1. Traverse the left subtree first by recursively calling the helper function on the left child.
        2. Increment the counter when visiting a node.
        3. If the counter equals `k`, store the node's value as the k-th smallest element.
        4. Traverse the right subtree by recursively calling the helper function on the right child.

```pseudo
function kthSmallest(root, k):
	count = 0
	result = null

	function inorder(node):
		if node is null or result is not null:
			return

		inorder(node.left)
		count = count + 1

		if count == k:
			result = node.val
			return

		inorder(node.right)

	inorder(root)
	return result
```
