# Blind75: Clone Graph

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.

The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, node values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.

**Example 1:**

-   **Input**: `adjList = [[2],[1,3],[2]]`
-   **Output**: `[[2],[1,3],[2]]`
-   **Explanation**:
    -   There are 3 nodes in the graph.
    -   Node 1: `val = 1` and `neighbors = [2]`.
    -   Node 2: `val = 2` and `neighbors = [1, 3]`.
    -   Node 3: `val = 3` and `neighbors = [2]`.

**Example 2:**

-   **Input**: `adjList = [[]]`
-   **Output**: `[[]]`
-   **Explanation**: The graph has one node with no neighbors.

**Example 3:**

-   **Input**: `adjList = []`
-   **Output**: `[]`
-   **Explanation**: The graph is empty.

### Constraints

-   `0 <= The number of nodes in the graph <= 100`
-   `1 <= Node.val <= 100`
-   There are no duplicate edges and no self-loops in the graph.

### Approach 1: Depth-First Search (DFS) with HashMap

-   **Time Complexity**: `O(V + E)` where `V` is the number of nodes (vertices) and `E` is the number of edges.
-   **Space Complexity**: `O(V)` where `V` is the number of nodes (vertices).
-   **Description**: Perform a DFS to create a deep copy of the graph. Use a HashMap to keep track of visited nodes and their corresponding copies.
-   **Algorithm**:

    1.  If the input node is `none`, return `none`.
    2.  Create a HashMap `visited` to store the mapping of original nodes to their copies.
    3.  Define a recursive function `clone(node)`:
        -   If `node` is already in `visited`, return the corresponding copy.
        -   Create a new node with the same value as `node`.
        -   Add the new node to `visited`.
        -   Iterate over each neighbor of `node` and recursively clone them, adding the clones to the neighbors of the new node.
        -   Return the new node.
    4.  Call `clone` with the input node and return the result.

```pseudo
function cloneGraph(node):
	if node is none:
		return none

	visited = {}

	function clone(node):
		if node in visited:
			return visited[node]

		cloneNode = Node(node.val, [])
		visited[node] = cloneNode

		for neighbor in node.neighbors:
			cloneNode.neighbors.append(clone(neighbor))
		return cloneNode

	return clone(node)
```
