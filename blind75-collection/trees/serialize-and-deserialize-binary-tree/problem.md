# Blind75: Serialize and Deserialize Binary Tree

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.

**Note:** The input/output format in the examples is the same as how NeetCode serializes a binary tree. You do not necessarily need to follow this format.

**Example 1:**

-   **Input:** `root = [1,2,3,null,null,4,5]`
-   **Output:** `[1,2,3,null,null,4,5]`

**Example 2:**

-   **Input:** `root = []`
-   **Output:** `[]`

### Constraints

-   `0 <= The number of nodes in the tree <= 1000.`
-   `-1000 <= Node.val <= 1000`

---

### Approach 1: Level Order Serialization

-   **Time Complexity:** `O(n)`, where `n` is the number of nodes in the tree.
-   **Space Complexity:** `O(n)` for storing the serialized data and the queue used during deserialization.
-   **Description:** This approach serializes the tree by performing a level order traversal, where `null` values represent missing nodes. During deserialization, the string is split into values, and nodes are reconstructed in level order using a queue.
-   **Algorithm:**

    1. **Serialization:**

        1. If the root is `null`, return an empty string.
        2. Initialize an empty queue and add the root node to it.
        3. Initialize an empty list to store serialized values.
        4. While the queue is not empty:
            1. Dequeue a node.
            2. If the node is `null`, add `"null"` to the list of serialized values.
            3. Otherwise, add the node's value to the list and enqueue its left and right children.
        5. Return the serialized values joined by commas.

    2. **Deserialization:**
        1. If the data is an empty string, return `null`.
        2. Split the data into a list of values.
        3. Create the root node using the first value and initialize a queue with the root.
        4. While there are more values to process:
            1. Dequeue a node.
            2. If the next value is not `"null"`, create the left child node and enqueue it.
            3. If the next value is not `"null"`, create the right child node and enqueue it.
        5. Return the root node.

```pseudo
function serialize(root):
	if root is null:
		return ""

	queue = []
	queue.push(root)
	serialized = []

	while not queue.isEmpty():
		node = queue.pop()

		if node is null:
			serialized.append("null")
		else:
			serialized.append(str(node.val))
			queue.push(node.left)
			queue.push(node.right)

	return serialized.join(",")

function deserialize(data):
	if data is empty:
		return null

	values = data.split(",")
	root = new TreeNode(int(values[0]))
	queue = []
	queue.push(root)
	i = 1

	while i < len(values):
		node = queue.pop()

		if values[i] != "null":
			node.left = new TreeNode(int(values[i]))
			queue.push(node.left)
		i += 1

		if i < len(values) and values[i] != "null":
			node.right = new TreeNode(int(values[i]))
			queue.push(node.right)
		i += 1

	return root
```

---

### Approach 2: Preorder Traversal Serialization

-   **Time Complexity:** `O(n)`, where `n` is the number of nodes in the tree.
-   **Space Complexity:** `O(n)` for storing the serialized data and the recursive call stack during deserialization.
-   **Description:** This approach uses a preorder traversal for serialization and deserialization. In serialization, nodes are visited in root-left-right order, with `null` values representing missing nodes. During deserialization, the serialized string is split into values, and the tree is reconstructed by recursively assigning values to nodes.
-   **Algorithm:**

    1. **Serialization:**

        1. Define a helper function that performs preorder traversal.
        2. If the node is `null`, append `"null"` to the serialized list.
        3. Otherwise, append the node's value and recursively traverse its left and right children.
        4. Return the serialized values joined by commas.

    2. **Deserialization:**
        1. Split the serialized string into a list of values.
        2. Define a helper function that constructs the tree using preorder traversal.
        3. If the current value is `"null"`, return `null`.
        4. Create a node with the current value and recursively assign its left and right children.
        5. Return the root node.

```pseudo
function serialize(root):
	def preorder(node):
		if node is null:
			serialized.append("null")
		else:
			serialized.append(str(node.val))
			preorder(node.left)
			preorder(node.right)

	serialized = []
	preorder(root)
	return serialized.join(",")

function deserialize(data):
	values = data.split(",")
	index = 0

	def build():
		if values[index] == "null":
			index += 1
			return null

		node = new TreeNode(int(values[index]))
		index += 1
		node.left = build()
		node.right = build()

		return node

	return build()
```
