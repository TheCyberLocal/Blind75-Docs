# Blind75: Subtree of Another Tree

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given the roots of two binary trees `root` and `sub_root`, return `True` if there is a subtree of `root` with the same structure and node values as `sub_root`, and `False` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

**Example 1:**

- **Input:** `root = [1,2,3,4,5], sub_root = [2,4,5]`
- **Output:** `True`

**Example 2:**

- **Input:** `root = [1,2,3,4,5,None,None,6], sub_root = [2,4,5]`
- **Output:** `False`

### Constraints

- `0 <= The number of nodes in both trees <= 100.`
- `-100 <= root.val, sub_root.val <= 100`

---

### Approach 1: Recursive Subtree Check

- **Time Complexity:** `O(m * n)`, where `m` is the number of nodes in `root` and `n` is the number of nodes in `sub_root`.
- **Space Complexity:** `O(h)` for the recursive call stack, where `h` is the height of `root`.
- **Description:** This approach uses recursion to check whether `sub_root` is a subtree of `root`. For each node in `root`, it checks if the current subtree rooted at this node is identical to `sub_root`. If not, it recursively checks the left and right children of the current node.
- **Algorithm:**

  1. **Is Same Tree Check:**

     1. Define a helper function `is_same_tree` that checks if two trees are identical.
     2. If both nodes are `None`, return `True`.
     3. If one node is `None` and the other is not, return `False`.
     4. If the values of the nodes are different, return `False`.
     5. Recursively check the left and right subtrees.

  2. **Subtree Check:**
     1. If `root` is `None`, return `False`.
     2. If `is_same_tree(root, sub_root)` returns `True`, return `True`.
     3. Recursively check the left and right subtrees of `root`.
     4. Return `False` if `sub_root` is not found in any subtree.

```python
def is_same_tree(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
	if tree1 is None and tree2 is None:
		return True
	if tree1 is None or tree2 is None:
		return False
	if tree1.val != tree2.val:
		return False
	return is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right)

def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
	if root is None:
		return False
	if is_same_tree(root, sub_root):
		return True
	return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)
```

---

### Approach 2: Preorder Traversal with String Matching

- **Time Complexity:** `O(m + n)`, where `m` is the number of nodes in `root` and `n` is the number of nodes in `sub_root`.
- **Space Complexity:** `O(m + n)` for storing the serialized strings.
- **Description:** This approach serializes both `root` and `sub_root` using a preorder traversal and then checks if the serialized string of `sub_root` is a substring of the serialized string of `root`. Special markers are used for `None` nodes to ensure that different tree structures with the same values do not produce the same serialized string.
- **Algorithm:**

  1. **Serialization:**

     1. Define a helper function `serialize` that performs a preorder traversal.
     2. If the current node is `None`, append a marker (e.g., `"#"`) to the serialized string.
     3. Otherwise, append the node’s value and recursively serialize its left and right children.

  2. **Subtree Check:**
     1. Serialize both `root` and `sub_root`.
     2. Check if the serialized string of `sub_root` is a substring of the serialized string of `root`.
     3. Return `True` if it is, otherwise return `False`.

```python
def serialize(root: Optional[TreeNode]) -> str:
	if root is None:
		return "#"

	return str(root.val) + "," + serialize(root.left) + "," + serialize(root.right)

def isSubtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
	root_serialized = serialize(root)
	sub_root_serialized = serialize(sub_root)

	return sub_root_serialized in root_serialized
```
