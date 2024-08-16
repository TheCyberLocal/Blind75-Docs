# Blind75: Subtree of Another Tree

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values as `subRoot`, and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

**Example 1:**

-   **Input:** `root = [1,2,3,4,5], subRoot = [2,4,5]`
-   **Output:** `true`

**Example 2:**

-   **Input:** `root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]`
-   **Output:** `false`

### Constraints

-   `0 <= The number of nodes in both trees <= 100.`
-   `-100 <= root.val, subRoot.val <= 100`

---

### Approach 1: Recursive Subtree Check

-   **Time Complexity:** `O(m * n)`, where `m` is the number of nodes in `root` and `n` is the number of nodes in `subRoot`.
-   **Space Complexity:** `O(h)` for the recursive call stack, where `h` is the height of `root`.
-   **Description:** This approach uses recursion to check whether `subRoot` is a subtree of `root`. For each node in `root`, it checks if the current subtree rooted at this node is identical to `subRoot`. If not, it recursively checks the left and right children of the current node.
-   **Algorithm:**

    1. **Is Same Tree Check:**

        1. Define a helper function `isSameTree` that checks if two trees are identical.
        2. If both nodes are `null`, return `true`.
        3. If one node is `null` and the other is not, return `false`.
        4. If the values of the nodes are different, return `false`.
        5. Recursively check the left and right subtrees.

    2. **Subtree Check:**
        1. If `root` is `null`, return `false`.
        2. If `isSameTree(root, subRoot)` returns `true`, return `true`.
        3. Recursively check the left and right subtrees of `root`.
        4. Return `false` if `subRoot` is not found in any subtree.

```pseudo
function isSameTree(tree1, tree2):
	if tree1 is null and tree2 is null:
		return true
	if tree1 is null or tree2 is null:
		return false
	if tree1.val != tree2.val:
		return false
	return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)

function isSubtree(root, subRoot):
	if root is null:
		return false
	if isSameTree(root, subRoot):
		return true
	return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
```

---

### Approach 2: Preorder Traversal with String Matching

-   **Time Complexity:** `O(m + n)`, where `m` is the number of nodes in `root` and `n` is the number of nodes in `subRoot`.
-   **Space Complexity:** `O(m + n)` for storing the serialized strings.
-   **Description:** This approach serializes both `root` and `subRoot` using a preorder traversal and then checks if the serialized string of `subRoot` is a substring of the serialized string of `root`. Special markers are used for `null` nodes to ensure that different tree structures with the same values do not produce the same serialized string.
-   **Algorithm:**

    1. **Serialization:**

        1. Define a helper function `serialize` that performs a preorder traversal.
        2. If the current node is `null`, append a marker (e.g., `"#"`) to the serialized string.
        3. Otherwise, append the node’s value and recursively serialize its left and right children.

    2. **Subtree Check:**
        1. Serialize both `root` and `subRoot`.
        2. Check if the serialized string of `subRoot` is a substring of the serialized string of `root`.
        3. Return `true` if it is, otherwise return `false`.

```pseudo
function serialize(root):
	if root is null:
		return "#"

	return str(root.val) + "," + serialize(root.left) + "," + serialize(root.right)

function isSubtree(root, subRoot):
	rootSerialized = serialize(root)
	subRootSerialized = serialize(subRoot)

	return subRootSerialized in rootSerialized
```
