# Blind75: Kth Smallest Element in a BST

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given the root of a binary search tree (BST) and an integer `k`, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

- The left subtree of every node contains only nodes with keys less than the node's key.
- The right subtree of every node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees are also binary search trees.

**Example 1:**

- **Input:** `root = [2,1,3], k = 1`
- **Output:** `1`

**Example 2:**

- **Input:** `root = [4,3,5,2,null], k = 4`
- **Output:** `5`

### Constraints

- `1 <= k <= The number of nodes in the tree <= 1000`
- `0 <= Node.val <= 1000`

---

### Approach 1: Iterative Inorder Traversal

- **Time Complexity:** `O(n)` where `n` is the number of nodes in the tree.
- **Space Complexity:** `O(h)` where `h` is the height of the tree due to the stack used for traversal.
- **Description:** To find the k-th smallest element in a binary search tree (BST), we utilize an iterative inorder traversal. Inorder traversal naturally visits nodes in increasing order in a BST. By keeping track of the number of nodes visited, we can determine when we have reached the k-th smallest element.

- **Algorithm:**
  1.  Initialize an empty stack to assist in the iterative traversal and set the current node to the root.
  2.  Use a loop to perform the inorder traversal:
      1. Traverse the left subtree by pushing the current node to the stack and moving to its left child.
      2. Once there are no more left children, pop the last node from the stack (which is the current node to visit).
      3. Decrement `k` by 1 each time a node is visited.
      4. If `k` reaches 0, return the value of the current node as it is the k-th smallest element.
      5. Move to the right subtree of the current node and continue the traversal.

```python
def kth_smallest(root: Optional[TreeNode], k: int) -> int:
	stack = []
	curr = root

	while stack or curr:
		while curr:
			stack.append(curr)
			curr = curr.left

		curr = stack.pop()
		k -= 1

		if k == 0:
			return curr.val

		curr = curr.right
```
