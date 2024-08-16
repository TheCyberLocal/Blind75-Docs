# Blind75: Valid Binary Search Tree

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given the `root` of a binary tree, return `true` if it is a valid binary search tree (BST), otherwise return `false`.

A valid binary search tree satisfies the following constraints:

-   The left subtree of every node contains only nodes with keys less than the node's key.
-   The right subtree of every node contains only nodes with keys greater than the node's key.
-   Both the left and right subtrees are also binary search trees.

**Example 1:**

-   **Input:** `root = [2,1,3]`
-   **Output:** `true`

**Example 2:**

-   **Input:** `root = [1,2,3]`
-   **Output:** `false`
-   **Explanation:** The root node's value is `1`, but its left child's value is `2`, which is greater than `1`.

### Constraints

-   `1 <= The number of nodes in the tree <= 1000.`
-   `-1000 <= Node.val <= 1000`

---

### Approach 1: Recursive In-Order Traversal with Range Checking

-   **Time Complexity:** `O(n)`, where `n` is the number of nodes in the tree.
-   **Space Complexity:** `O(h)`, where `h` is the height of the tree, due to the recursion stack.
-   **Description:** This approach verifies that the tree satisfies the properties of a BST by ensuring that each node's value falls within a valid range. The valid range is adjusted as the tree is traversed:
    -   For a given node, the left child must be smaller than the node's value.
    -   The right child must be greater than the node's value.
    -   As the algorithm traverses down the tree, it updates the allowed range for each subtree accordingly.
-   **Algorithm:**

    1. Start from the `root` node with the initial range set to negative and positive infinity.
    2. Recursively check each node:
        1. If the node is `null`, return `true` (an empty tree is a valid BST).
        2. Check if the node’s value lies within the current valid range.
        3. Recursively check the left subtree, ensuring that all values are less than the current node’s value.
        4. Recursively check the right subtree, ensuring that all values are greater than the current node’s value.
    3. If all checks pass, return `true`; otherwise, return `false`.

```pseudo
function isValidBST(root):
    function validate(node, lowerBound, upperBound):
        if node is null:
            return true

        if node.val <= lowerBound or node.val >= upperBound:
            return false

        return validate(node.left, lowerBound, node.val) and validate(node.right, node.val, upperBound)

    return validate(root, -infinity, +infinity)
```

---

### Approach 2: Iterative In-Order Traversal

-   **Time Complexity:** `O(n)`, where `n` is the number of nodes in the tree.
-   **Space Complexity:** `O(h)`, where `h` is the height of the tree, for the stack used in traversal.
-   **Description:** An in-order traversal of a BST produces a sorted sequence of values. This approach uses an iterative in-order traversal to ensure that the sequence of node values encountered is strictly increasing.
-   **Algorithm:**

    1. Initialize an empty stack and set the `prevNode` to `null`.
    2. Traverse the tree in an in-order fashion:
        1. Push all left children onto the stack until a `null` node is reached.
        2. Pop the stack to visit a node.
        3. Check if the current node’s value is greater than the value of `prevNode`. If not, return `false`.
        4. Set `prevNode` to the current node.
        5. Move to the right child and repeat the process.
    3. If the traversal completes without violations, return `true`.

```pseudo
function isValidBST(root):
    stack = []
    prevNode = null

    while stack is not empty or root is not null:
        while root is not null:
            stack.push(root)
            root = root.left

        root = stack.pop()

        if prevNode is not null and root.val <= prevNode.val:
            return false

        prevNode = root
        root = root.right

    return true
```
