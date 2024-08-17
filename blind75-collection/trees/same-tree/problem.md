# Blind75: Same Tree

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given the roots of two binary trees `p` and `q`, return `true` if the trees are equivalent, otherwise return `false`.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

**Example 1:**

-   **Input:** `p = [1,2,3], q = [1,2,3]`
-   **Output:** `true`

**Example 2:**

-   **Input:** `p = [4,7], q = [4,null,7]`
-   **Output:** `false`

**Example 3:**

-   **Input:** `p = [1,2,3], q = [1,3,2]`
-   **Output:** `false`

### Constraints

-   `0 <= The number of nodes in both trees <= 100.`
-   `-100 <= Node.val <= 100`

---

### Approach 1: Recursive Comparison

-   **Time Complexity:** `O(n)`, where `n` is the number of nodes in the trees.
-   **Space Complexity:** `O(h)`, where `h` is the height of the tree, for the recursive call stack.
-   **Description:** This approach recursively compares each node of the two trees. If both nodes are `null`, they are considered equivalent. If only one node is `null`, or if the node values differ, the trees are not equivalent. The algorithm recursively checks the left and right subtrees for equivalence.
-   **Algorithm:**

    1. Start at the roots of both trees `p` and `q`.
    2. If both nodes are `null`, return `true`.
    3. If one of the nodes is `null` and the other is not, return `false`.
    4. If the values of `p` and `q` are different, return `false`.
    5. Recursively compare the left subtrees of `p` and `q`.
    6. Recursively compare the right subtrees of `p` and `q`.
    7. Return `true` if both subtrees are equivalent; otherwise, return `false`.

```pseudo
function isSameTree(p, q):
	if p is null and q is null:
		return true

	if p is null or q is null or p.val != q.val:
		return false

	return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```
