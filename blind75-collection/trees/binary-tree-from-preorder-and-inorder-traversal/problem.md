# Blind75: Binary Tree from Preorder and Inorder Traversal

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given two integer arrays `preorder` and `inorder`.

- `preorder` is the preorder traversal of a binary tree.
- `inorder` is the inorder traversal of the same tree.

Both arrays are of the same size and consist of unique values.

Rebuild the binary tree from the preorder and inorder traversals and return its root.

**Example 1:**

- **Input:** `preorder = [1,2,3,4]`, `inorder = [2,1,3,4]`
- **Output:** `[1,2,3,None,None,None,4]`

**Example 2:**

- **Input:** `preorder = [1]`, `inorder = [1]`
- **Output:** `[1]`

### Constraints

- `1 <= len(inorder) <= 1000`
- `len(inorder) == len(preorder)`
- `-1000 <= preorder[i], inorder[i] <= 1000`

---

### Approach 1: Recursive Tree Construction

- **Time Complexity:** `O(n)` where `n` is the number of nodes in the tree.
- **Space Complexity:** `O(n)` for the recursive call stack and hashmap storage.
- **Description:** The problem can be solved by recognizing that the first element in the `preorder` array is always the root of the tree. The position of this root in the `inorder` array determines the division of the left and right subtrees. Recursively apply this process to construct the entire tree.
- **Algorithm:**

  1. Create a hashmap to store the index of each value in the `inorder` array for quick lookup.
  2. Define a recursive helper function that constructs the tree:
     - The base case occurs when there are no elements to process.
     - The root is selected as the first element of the current `preorder` array.
     - The left and right subtrees are then recursively constructed based on the division determined by the root's position in the `inorder` array.
  3. The final result is the root of the constructed binary tree.

```python
def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
	index_map = {value: index for index, value in enumerate(inorder)}

	def build_subtree(pre_start: int, pre_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
		if pre_start > pre_end or in_start > in_end:
			return None

		root_val = preorder[pre_start]
		root = TreeNode(root_val)
		in_index = index_map[root_val]
		left_size = in_index - in_start

		root.left = build_subtree(pre_start + 1, pre_start + left_size, in_start, in_index - 1)
		root.right = build_subtree(pre_start + left_size + 1, pre_end, in_index + 1, in_end)

		return root

	return build_subtree(0, len(preorder) - 1, 0, len(inorder) - 1)
```
