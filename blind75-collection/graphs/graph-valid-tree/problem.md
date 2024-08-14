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

### Approach 1: Union-Find

-   **Time Complexity**: `O(V + E)` where `V` is the number of nodes and `E` is the number of edges.
-   **Space Complexity**: `O(V)` for the parent and rank arrays.
-   **Description**: To check if the graph is a valid tree, we can use the Union-Find data structure to detect cycles. A valid tree has exactly `n-1` edges and is fully connected without any cycles. Union-Find helps efficiently check for cycles as we try to unify nodes.
-   **Algorithm**:

	1. If the number of edges is not equal to `n - 1`, return `false`.
	2. Initialize the `parent` array where each node is its own parent.
	3. Initialize the `rank` array to store the rank (height) of each tree.
	4. Define the `find(x)` function to find the root of `x`.
	5. Define the `union(x, y)` function to unite the sets containing `x` and `y`.
		- Find the roots of `x` and `y`.
		- If they have the same root, a cycle exists, so return `false`.
		- Otherwise, unite the sets based on rank and update the parent and rank arrays.
	6. Iterate through the edges, applying `union` on each pair.
	7. If no cycle is detected, return `true`.

```pseudo
function validTree(n, edges):
	if len(edges) != n - 1:
		return False

	parent = [i for i in range(n)]
	rank = [1] * n

	function find(x):
		if parent[x] != x:
			parent[x] = find(parent[x])
		return parent[x]

	function union(x, y):
		rootX = find(x)
		rootY = find(y)
		if rootX == rootY:
			return False

		if rank[rootX] > rank[rootY]:
			parent[rootY] = rootX
		elif rank[rootX] < rank[rootY]:
			parent[rootX] = rootY
		else:
			parent[rootY] = rootX
			rank[rootX] += 1

		return True

	for x, y in edges:
		if not union(x, y):
			return False

	return True
```

### Approach 2: Depth-First Search (DFS)

-   **Time Complexity**: `O(V + E)` where `V` is the number of nodes and `E` is the number of edges.
-   **Space Complexity**: `O(V + E)` to store the graph and visited set.
-   **Description**: Using DFS, we can explore the graph and ensure that it is fully connected and acyclic. We use a visited set to track visited nodes and avoid revisiting them.
-   **Algorithm**:

	1. If the number of edges is not equal to `n - 1`, return `false`.
	2. Build the adjacency list from the edges.
	3. Define a recursive `dfs(node, parent)` function:
		- Mark `node` as visited.
		- Recursively visit all its neighbors.
		- If a visited neighbor is not the parent, a cycle is detected, so return `false`.
	4. Start DFS from node `0`.
	5. After the DFS, check if all nodes are visited.
	6. If all nodes are visited and no cycles were detected, return `true`.

```pseudo
function validTree(n, edges):
	if len(edges) != n - 1:
		return False

	graph = {i: [] for i in range(n)}
	visited = set()

	for x, y in edges:
		graph[x].append(y)
		graph[y].append(x)

	function dfs(node, parent):
		visited.add(node)
		for neighbor in graph[node]:
			if neighbor == parent:
				continue
			if neighbor in visited or not dfs(neighbor, node):
				return False
		return True

	if not dfs(0, -1):
		return False

	return len(visited) == n
```
