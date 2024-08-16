# Blind75: Lowest Common Ancestor of a BST

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a binary search tree (BST) where all node values are unique, and two nodes from the tree `p` and `q`, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes `p` and `q` is the lowest node in a tree `T` such that both `p` and `q` are descendants. The ancestor is allowed to be a descendant of itself.

**Example 1:**

-   **Input:** `root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8`
-   **Output:** `5`

**Example 2:**

-   **Input:** `root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4`
-   **Output:** `3`
-   **Explanation:** The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.

### Constraints

-   `2 <= The number of nodes in the tree <= 100.`
-   `-100 <= Node.val <= 100`
-   `p != q`
-   `p` and `q` will both exist in the BST.

---

### Approach: Recursive Search

-   **Time Complexity:** `O(h)`, where `h` is the height of the tree.
-   **Space Complexity:** `O(h)` for the recursive call stack.
-   **Description:** This approach leverages the properties of a BST to find the LCA. Given that the values in the left subtree are always smaller than the root, and the values in the right subtree are always larger, the LCA can be determined based on the values of `p` and `q`. Starting at the root, if both `p` and `q` are smaller than the root, the LCA must be in the left subtree. Conversely, if both are larger, the LCA is in the right subtree. If `p` and `q` are on opposite sides of the root, the root itself is their LCA.
-   **Algorithm:**

    1. Start at the root of the tree.
    2. Compare the values of `p` and `q` with the value of the current node.
        1. If both `p` and `q` are smaller, move to the left subtree.
        2. If both `p` and `q` are larger, move to the right subtree.
        3. If one is smaller and the other is larger, the current node is the LCA.
    3. Return the current node as the LCA.

```pseudo
function lowestCommonAncestor(root, p, q):
	if root is None:
		return None

	if p.val < root.val and q.val < root.val:
		return lowestCommonAncestor(root.left, p, q)

	if p.val > root.val and q.val > root.val:
		return lowestCommonAncestor(root.right, p, q)

	return root
```
