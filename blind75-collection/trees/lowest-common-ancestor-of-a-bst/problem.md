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

### Approach 1: Iterative Search

-   **Time Complexity:** `O(h)`, where `h` is the height of the tree.
-   **Space Complexity:** `O(1)` as the search is performed iteratively with constant space.
-   **Description:** This approach efficiently finds the Lowest Common Ancestor (LCA) in a Binary Search Tree (BST) by leveraging its structural properties. In a BST, nodes in the left subtree have values less than the root, and nodes in the right subtree have values greater than the root. By iteratively traversing the tree, we can identify the LCA based on the values of `p` and `q`. If both values are smaller than the current node, the LCA lies in the left subtree. If both are larger, it lies in the right subtree. If the values diverge, with one on either side of the current node, the current node is the LCA.
-   **Algorithm:**

    1.  Start with the root node as the current node.
    2.  Enter a loop to traverse the tree:
        1. If both `p` and `q` have values smaller than the current node’s value, move to the right subtree by setting the current node to its right child.
        2. If both `p` and `q` have values larger than the current node’s value, move to the left subtree by setting the current node to its left child.
        3. If one value is smaller and the other is larger (or one matches the current node), the current node is the LCA.
    3.  Return the current node as the LCA.

```pseudo
function lowestCommonAncestor(root, p, q):
	while True:
		if root.val < p.val and root.val < q.val:
			root = root.right
		else if root.val > p.val and root.val > q.val:
			root = root.left
		else:
			return root
```
