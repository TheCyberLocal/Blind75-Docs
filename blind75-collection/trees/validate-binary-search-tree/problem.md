# Blind75: Valid Binary Search Tree

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given the `root` of a binary tree, return `True` if it is a valid binary search tree (BST), otherwise return `False`.

A valid binary search tree satisfies the following constraints:

- The left subtree of every node contains only nodes with keys less than the node's key.
- The right subtree of every node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees are also binary search trees.

**Example 1:**

- **Input:** `root = [2,1,3]`
- **Output:** `True`

**Example 2:**

- **Input:** `root = [1,2,3]`
- **Output:** `False`
- **Explanation:** The root node's value is `1`, but its left child's value is `2`, which is greater than `1`.

### Constraints

- `1 <= The number of nodes in the tree <= 1000.`
- `-1000 <= Node.val <= 1000`

---

### Approach 1: Recursive In-Order Traversal with Range Checking

- **Time Complexity:** `O(n)`, where `n` is the number of nodes in the tree.
- **Space Complexity:** `O(h)`, where `h` is the height of the tree, due to the recursion stack.
- **Description:** This approach verifies that the tree satisfies the properties of a BST by ensuring that each node's value falls within a valid range. The valid range is adjusted as the tree is traversed:
  - For a given node, the left child must be smaller than the node's value.
  - The right child must be greater than the node's value.
  - As the algorithm traverses down the tree, it updates the allowed range for each subtree accordingly.
- **Algorithm:**

  1. Start from the `root` node with the initial range set to negative and positive infinity.
  2. Recursively check each node:
     1. If the node is `None`, return `True` (an empty tree is a valid BST).
     2. Check if the node’s value lies within the current valid range.
     3. Recursively check the left subtree, ensuring that all values are less than the current node’s value.
     4. Recursively check the right subtree, ensuring that all values are greater than the current node’s value.
  3. If all checks pass, return `True`; otherwise, return `False`.

```python
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def validate(node: Optional[TreeNode], lower_bound: float, upper_bound: float) -> bool:
        if node is None:
            return True

        if node.val <= lower_bound or node.val >= upper_bound:
            return False

        return validate(node.left, lower_bound, node.val) and validate(node.right, node.val, upper_bound)

    return validate(root, float("-inf"), float("inf"))
```

---

### Approach 2: Iterative In-Order Traversal

- **Time Complexity:** `O(n)`, where `n` is the number of nodes in the tree.
- **Space Complexity:** `O(h)`, where `h` is the height of the tree, for the stack used in traversal.
- **Description:** An in-order traversal of a BST produces a sorted sequence of values. This approach uses an iterative in-order traversal to ensure that the sequence of node values encountered is strictly increasing.
- **Algorithm:**

  1. Initialize an empty stack and set the `prev_node` to `None`.
  2. Traverse the tree in an in-order fashion:
     1. Push all left children onto the stack until a `None` node is reached.
     2. Pop the stack to visit a node.
     3. Check if the current node’s value is greater than the value of `prev_node`. If not, return `False`.
     4. Set `prev_node` to the current node.
     5. Move to the right child and repeat the process.
  3. If the traversal completes without violations, return `True`.

```python
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    stack = []
    prev_node = None

    while stack or root is not None:
        while root is not None:
            stack.push(root)
            root = root.left

        root = stack.pop()

        if prev_node is not None and root.val <= prev_node.val:
            return False

        prev_node = root
        root = root.right

    return True
```
