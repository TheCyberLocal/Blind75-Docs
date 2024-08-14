# Blind75: Graph Valid Tree

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

**Example 1:**

-   **Input**: `n = 5`, `edges = [[0, 1], [0, 2], [0, 3], [1, 4]]`
-   **Output**: `true`

**Example 2:**

-   **Input**: `n = 5`, `edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]`
-   **Output**: `false`

### Note

-   You can assume that no duplicate edges will appear in edges. Since all edges are undirected, `[0, 1]` is the same as `[1, 0]` and thus will not appear together in edges.

### Constraints

-   `1 <= n <= 100`
-   `0 <= len(edges) <= n * (n - 1) / 2`

---

### Approach 1: Union-Find

-   **Time Complexity**: `O(V + E)` where `V` is the number of nodes and `E` is the number of edges.
-   **Space Complexity**: `O(V)` for the parent and rank arrays.
-   **Description**: To check if the graph is a valid tree, we can use the Union-Find data structure to detect cycles. A valid tree has exactly `n-1` edges and is fully connected without any cycles. Union-Find helps efficiently check for cycles as we try to unify nodes.
-   **Algorithm**:

    1.  If the number of edges is not equal to `n - 1`, return `false`.
    2.  Initialize the `parent` array where each node is its own parent.
    3.  Initialize the `rank` array to store the rank (height) of each tree.
    4.  Define the `find(x)` function to find the root of `x`.
    5.  Define the `union(n1, n2)` function to unite the sets containing `n1` and `n2`.
        -   Find the roots (parents) of `n1` and `n2`.
        -   If they have the same root, a cycle exists, so return `false`.
        -   Otherwise, unite the sets based on rank and update the parent and rank arrays.
    6.  Iterate through the edges, applying `union` on each pair.
    7.  If no cycle is detected, return `true`.

```pseudo
function validTree(n, edges):
	if len(edges) != n - 1:
		return false

	parent = an array of size n initialized by index
	rank = an array of size n initialized to 1

	function find(x):
		if parent[x] != x:
			parent[x] = find(parent[x])
		return parent[x]

	function union(n1, n2):
		p1 = find(n1)
		p2 = find(n2)
		if p1 == p2:
			return false

		if rank[p1] > rank[p2]:
			parent[p2] = p1
		else if rank[p1] < rank[p2]:
			parent[p1] = p2
		else:
			parent[p2] = p1
			rank[p1] += 1

		return true

	for x, y in edges:
		if not union(x, y):
			return false

	return true
```

---

### Approach 2: Depth-First Search (DFS)

-   **Time Complexity**: `O(V + E)` where `V` is the number of nodes and `E` is the number of edges.
-   **Space Complexity**: `O(V + E)` to store the graph and visited set.
-   **Description**: Using DFS, we can explore the graph and ensure that it is fully connected and acyclic. We use a visited set to track visited nodes and avoid revisiting them.
-   **Algorithm**:

    1.  If the number of edges is not equal to `n - 1`, return `false`.
    2.  Build the adjacency list from the edges.
    3.  Define a recursive `dfs(node, parent)` function:
        -   Mark `node` as visited.
        -   Recursively visit all its neighbors.
        -   If a visited neighbor is not the parent, a cycle is detected, so return `false`.
    4.  Start DFS from node `0`.
    5.  After the DFS, check if all nodes are visited.
    6.  If all nodes are visited and no cycles were detected, return `true`.

```pseudo
function validTree(n, edges):
	if len(edges) != n - 1:
		return false

	adj = a map of keys from 0 to n - 1 initialized to []
	visited = set()

	for x, y in edges:
		adj[x].append(y)
		adj[y].append(x)

	function dfs(node, parent):
		visited.add(node)
		for neighbor in adj[node]:
			if neighbor == parent:
				continue
			if neighbor in visited or not dfs(neighbor, node):
				return false
		return true

	if not dfs(0, -1):
		return false

	return len(visited) == n
```
