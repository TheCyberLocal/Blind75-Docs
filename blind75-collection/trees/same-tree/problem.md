# Blind75: Same Tree

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given the roots of two binary trees `p` and `q`, return `True` if the trees are equivalent, otherwise return `False`.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

**Example 1:**

-   **Input:** `p = [1,2,3], q = [1,2,3]`
-   **Output:** `True`

**Example 2:**

-   **Input:** `p = [4,7], q = [4,None,7]`
-   **Output:** `False`

**Example 3:**

-   **Input:** `p = [1,2,3], q = [1,3,2]`
-   **Output:** `False`

### Constraints

-   `0 <= The number of nodes in both trees <= 100.`
-   `-100 <= Node.val <= 100`

---

### Approach 1: Recursive Comparison

-   **Time Complexity:** `O(n)`, where `n` is the number of nodes in the trees.
-   **Space Complexity:** `O(h)`, where `h` is the height of the tree, for the recursive call stack.
-   **Description:** This approach recursively compares each node of the two trees. If both nodes are `None`, they are considered equivalent. If only one node is `None`, or if the node values differ, the trees are not equivalent. The algorithm recursively checks the left and right subtrees for equivalence.
-   **Algorithm:**

    1. Start at the roots of both trees `p` and `q`.
    2. If both nodes are `None`, return `True`.
    3. If one of the nodes is `None` and the other is not, return `False`.
    4. If the values of `p` and `q` are different, return `False`.
    5. Recursively compare the left subtrees of `p` and `q`.
    6. Recursively compare the right subtrees of `p` and `q`.
    7. Return `True` if both subtrees are equivalent; otherwise, return `False`.

```python
def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
	if p is None and q is None:
		return True

	if p is None or q is None or p.val != q.val:
		return False

	return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
```
