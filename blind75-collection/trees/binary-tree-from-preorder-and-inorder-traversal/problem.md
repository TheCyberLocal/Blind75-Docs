# Blind75: Binary Tree from Preorder and Inorder Traversal

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given two integer arrays `preorder` and `inorder`.

-   `preorder` is the preorder traversal of a binary tree.
-   `inorder` is the inorder traversal of the same tree.

Both arrays are of the same size and consist of unique values.

Rebuild the binary tree from the preorder and inorder traversals and return its root.

**Example 1:**

-   **Input:** `preorder = [1,2,3,4]`, `inorder = [2,1,3,4]`
-   **Output:** `[1,2,3,null,null,null,4]`

**Example 2:**

-   **Input:** `preorder = [1]`, `inorder = [1]`
-   **Output:** `[1]`

### Constraints

-   `1 <= len(inorder) <= 1000`
-   `len(inorder) == len(preorder)`
-   `-1000 <= preorder[i], inorder[i] <= 1000`

---

### Approach 1: Recursive Tree Construction

-   **Time Complexity:** `O(n)` where `n` is the number of nodes in the tree.
-   **Space Complexity:** `O(n)` for the recursive call stack and hashmap storage.
-   **Description:** The problem can be solved by recognizing that the first element in the `preorder` array is always the root of the tree. The position of this root in the `inorder` array determines the division of the left and right subtrees. Recursively apply this process to construct the entire tree.
-   **Algorithm:**

    1. Create a hashmap to store the index of each value in the `inorder` array for quick lookup.
    2. Define a recursive helper function that constructs the tree:
        - The base case occurs when there are no elements to process.
        - The root is selected as the first element of the current `preorder` array.
        - The left and right subtrees are then recursively constructed based on the division determined by the root's position in the `inorder` array.
    3. The final result is the root of the constructed binary tree.

```pseudo
function buildTree(preorder, inorder):
	indexMap = create a map to store (value -> index) for inorder

	function buildSubtree(preStart, preEnd, inStart, inEnd):
		if preStart > preEnd or inStart > inEnd:
			return null

		rootVal = preorder[preStart]
		root = new TreeNode(rootVal)
		inIndex = indexMap[rootVal]
		leftSize = inIndex - inStart

		root.left = buildSubtree(preStart + 1, preStart + leftSize, inStart, inIndex - 1)
		root.right = buildSubtree(preStart + leftSize + 1, preEnd, inIndex + 1, inEnd)

		return root

	return buildSubtree(0, len(preorder) - 1, 0, len(inorder) - 1)
```
